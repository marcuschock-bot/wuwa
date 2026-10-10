import streamlit as st
import requests
import pandas as pd
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="MongoDB Database Manager",
    page_icon="🍃",
    layout="wide",
    initial_sidebar_state="expanded"
)

BASE_URL = "http://127.0.0.1:8000"


def normalize_record(record):
    """Normalize MongoDB-style IDs and FastAPI-style IDs to a common shape."""
    if not isinstance(record, dict):
        return record

    normalized = dict(record)
    if "_id" not in normalized and "id" in normalized:
        normalized["_id"] = normalized["id"]
    if "id" not in normalized and "_id" in normalized:
        normalized["id"] = normalized["_id"]
    return normalized


def normalize_users(users):
    return [normalize_record(user) for user in users]


def normalize_posts(posts):
    return [normalize_record(post) for post in posts]


def check_api_connection():
    """Check if the FastAPI server is running"""
    try:
        response = requests.get(f"{BASE_URL}/")
        return response.status_code == 200
    except:
        return False

def create_user(name, email, age):
    """Create a new user in MongoDB"""
    try:
        response = requests.post(
            f"{BASE_URL}/users/",
            json={"name": name, "email": email, "age": age}
        )
        return response.json(), response.status_code == 200
    except Exception as e:
        return {"error": str(e)}, False

def get_all_users():
    """Get all users from MongoDB"""
    try:
        response = requests.get(f"{BASE_URL}/users/")
        if response.status_code == 200:
            return normalize_users(response.json()), True
        return [], False
    except Exception as e:
        return [], False


def get_user_posts(user_id):
    """Get posts for a specific user"""
    try:
        response = requests.get(f"{BASE_URL}/users/{user_id}/posts")
        if response.status_code == 200:
            return normalize_posts(response.json()), True
        return [], False
    except Exception as e:
        return [], False

def create_post(user_id, title, content):
    """Create a new post for user"""
    try:
        response = requests.post(
            f"{BASE_URL}/posts/",
            json={"user_id": user_id, "title": title, "content": content}
        )
        return response.json(), response.status_code == 200
    except Exception as e:
        return {"error": str(e)}, False

def get_all_posts():
    """Get all posts with user"""
    try:
        response = requests.get(f"{BASE_URL}/posts/")
        if response.status_code == 200:
            return normalize_posts(response.json()), True
        return [], False
    except Exception as e:
        return [], False

def delete_user_by_id(user_id):
    """Delete a user by ID"""
    try:
        response = requests.delete(f"{BASE_URL}/users/{user_id}")
        return response.json(), response.status_code == 200
    except Exception as e:
        return {"error": str(e)}, False

def delete_post(post_id):
    """Delete a post by ID"""
    try:
        response = requests.delete(f"{BASE_URL}/posts/{post_id}")
        return response.json(), response.status_code == 200
    except Exception as e:
        return {"error": str(e)}, False

def update_user_by_id(user_id, name, email, age):
    """Update a user by ID"""
    try:
        response = requests.put(
            f"{BASE_URL}/users/{user_id}",
            json={"name": name, "email": email, "age": age}
        )
        return response.json(), response.status_code == 200
    except Exception as e:
        return {"error": str(e)}, False

def main():
    st.title("🍃 MongoDB Database Manager")
    st.markdown("---")

    # Check API connection
    if not check_api_connection():
        st.error("❌ Cannot connect to FastAPI server. Please make sure it is running on http://127.0.0.1:8000")
        st.info("Run `uvicorn main:app --reload` to start the server.")
        return

    st.success("✅ Connected to FastAPI server!")

    # Sidebar navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox(
        "Choose a page",
        ["Users", "Posts", "Dashboard"]
    )

    if page == "Users":
        users_page()
    elif page == "Posts":
        posts_page()
    elif page == "Dashboard":
        dashboard_page()

def users_page():
    st.header("👥 User Management")

    # Tabs for different user operations
    tab1, tab2, tab3 = st.tabs(["Create User", "View Users", "Manage Users"])

    with tab1:
        st.subheader("Create New User")
        with st.form("create_user_form"):
            col1, col2 = st.columns(2)
            with col1:
                name = st.text_input("Name", placeholder="Enter user name")
                email = st.text_input("Email", placeholder="Enter email address")
            with col2:
                age = st.number_input("Age", min_value=1, max_value=120, value=25)

            submitted = st.form_submit_button("Create User", type="primary")

            if submitted:
                if name and email:
                    result, success = create_user(name, email, age)
                    if success:
                        st.success(f"✅ User created successfully! ID: {result.get('user_id')}")
                        st.rerun()
                    else:
                        st.error(f"❌ Error: {result.get('detail', 'Unknown error')}")
                else:
                    st.error("❌ Please fill in all required fields.")

    with tab2:
        st.subheader("All Users")
        users, success = get_all_users()

        if success and users:
            df = pd.DataFrame(users)
            if "_id" in df.columns:
                df["_id"] = df["_id"].apply(lambda x: str(x))
            if "id" in df.columns:
                df["id"] = df["id"].apply(lambda x: str(x))

            st.dataframe(
                df,
                use_container_width=True,
                hide_index=True
            )

            st.info(f"Total Users: {len(users)}")
        else:
            st.info("No users found.")

    with tab3:
        st.subheader("Manage Users")
        users, success = get_all_users()

        if success and users:
            user_options = {f"{user['name']} ({user['email']})": user for user in users}
            selected_user_display = st.selectbox("Select user", options=list(user_options.keys()))

            if selected_user_display:
                selected_user = user_options[selected_user_display]
                selected_user_id = selected_user.get("_id") or selected_user.get("id")

                col1, col2 = st.columns(2)

                with col1:
                    st.write("### Update User")
                    with st.form(f"update_form_{selected_user_id}"):
                        new_name = st.text_input("Name", value=selected_user["name"])
                        new_email = st.text_input("Email", value=selected_user["email"])
                        new_age = st.number_input("Age", min_value=1, max_value=120, value=selected_user["age"])

                        update_submitted = st.form_submit_button("Update User", type="primary")

                        if update_submitted:
                            result, success = update_user_by_id(selected_user_id, new_name, new_email, new_age)
                            if success:
                                st.success("✅ User updated successfully!")
                                st.rerun()
                            else:
                                st.error(f"❌ Error: {result.get('detail', 'Unknown error')}")

                with col2:
                    st.write("### Danger Zone")
                    st.warning("⚠️ This will delete the user and all their posts!")
                    if st.button("Delete User", type="secondary"):
                        result, success = delete_user_by_id(selected_user_id)
                        if success:
                            st.success("✅ User deleted successfully!")
                            st.rerun()
                        else:
                            st.error(f"❌ Error: {result.get('detail', 'Unknown error')}")
        else:
            st.info("No users to manage.")

def posts_page():
    st.header("📝 Post Management")

    tab1, tab2 = st.tabs(["Create Post", "View Posts"])

    with tab1:
        st.subheader("Create New Post")
        users, users_success = get_all_users()

        if users_success and users:
            with st.form("create_post_form"):
                user_options = {f"{user['name']} ({user['email']})": (user.get("_id") or user.get("id")) for user in users}
                selected_user_display = st.selectbox("Select Author", options=list(user_options.keys()))

                title = st.text_input("Title", placeholder="Enter post title")
                content = st.text_area("Content", placeholder="Enter post content", height=150)

                submitted = st.form_submit_button("Create Post", type="primary")

                if submitted:
                    if selected_user_display and title and content:
                        user_id = user_options[selected_user_display]
                        result, success = create_post(user_id, title, content)
                        if success:
                            st.success(f"✅ Post created successfully! ID: {result.get('post_id')}")
                            st.rerun()
                        else:
                            st.error(f"❌ Error: {result.get('detail', 'Unknown error')}")
                    else:
                        st.error("❌ Please fill in all fields.")
        else:
            st.warning("⚠️ No users found. Please create a new user first.")

    with tab2:
        st.subheader("All Posts")
        posts, success = get_all_posts()

        if success and posts:
            for post in posts:
                post_id = post.get("_id") or post.get("id")
                with st.expander(f"📌 {post.get('title', 'Untitled Post')} ({post.get('author_name', 'Unknown')})"):
                    col1, col2 = st.columns([4, 1])
                    with col1:
                        st.write(f"**Content:** {post.get('content')}")
                        st.write(f"**Created At:** {post.get('created_at', 'N/A')}")
                    with col2:
                        if st.button("Delete", key=f"delete_post_{post_id}", type="secondary"):
                            result, success = delete_post(post_id)
                            if success:
                                st.success("✅ Post deleted!")
                                st.rerun()
                            else:
                                st.error("❌ Failed to delete post")
        else:
            st.info("No posts found.")

def dashboard_page():
    st.header("📊 Dashboard")

    users, users_success = get_all_users()
    posts, posts_success = get_all_posts()

    if users_success and posts_success:
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric("Total Users", len(users))

        with col2:
            st.metric("Total Posts", len(posts))

        with col3:
            avg_age = sum(user.get("age", 0) for user in users) / len(users) if users else 0
            st.metric("Average User Age", f"{avg_age:.1f}")

        with col4:
            posts_per_user = len(posts) / len(users) if users else 0
            st.metric("Posts per User", f"{posts_per_user:.1f}")

        st.markdown("---")
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("User Age Distribution")
            age_data = [user.get("age", 0) for user in users]
            st.bar_chart(age_data)

        with col2:
            st.subheader("Recent Activity")
            if posts:
                df_posts = pd.DataFrame(posts)
                recent_posts = posts[-5:]
                for post in recent_posts:
                    st.write(f"📝 **{post.get('title')}** by {post.get('author_name', 'Unknown')}")
            else:
                st.info("No activity recorded yet.")
    else:
        st.error("❌ Failed to load dashboard data.")

if __name__ == "__main__":
    main()
    