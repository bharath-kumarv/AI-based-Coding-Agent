# auth.py - FIXED PHOTO DISPLAY + NARROW LOGIN + ALL FEATURES
import streamlit as st
import hashlib
import json
import os
from PIL import Image
import io

# ─────────────────────────────────────────────
# PERSISTENT USERS WITH PHOTOS
USERS_FILE = "users.json"

def load_users():
    try:
        if os.path.exists(USERS_FILE):
            with open(USERS_FILE, "r") as f:
                return json.load(f)
    except:
        pass
    return {
        "student": hashlib.sha256("password123".encode()).hexdigest(),
        "admin": hashlib.sha256("admin456".encode()).hexdigest(),
        "guest": hashlib.sha256("guest789".encode()).hexdigest()
    }

def save_users(users):
    try:
        with open(USERS_FILE, "w") as f:
            json.dump(users, f)
    except:
        pass

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def init_auth_state():
    defaults = {
        "authenticated": False,
        "username": None,
        "login_attempts": 0,
        "locked_out": False,
        "show_edit": False,
        "profile_photos": {}  # NEW: Store photos
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

def login_page():
    """NARROW PROFESSIONAL LOGIN + SIGNUP"""
    st.markdown("""
    <style>
    /* NARROW centered login - max 400px */
    section[data-testid="stHorizontalBlock"] {
        max-width: 400px !important;
        margin: 2rem auto !important;
        background: rgba(20,30,48,0.95) !important;
        padding: 2.5rem !important;
        border-radius: 18px !important;
        border: 2px solid rgba(255,215,0,0.3) !important;
        backdrop-filter: blur(20px) !important;
    }
    h1 { color: #FFD700 !important; font-size: 2rem !important; text-align: center !important; }
    .stTextInput input {
        background: rgba(255,255,255,0.12) !important;
        border: 2px solid rgba(255,215,0,0.3) !important;
        border-radius: 10px !important;
        color: white !important;
        padding: 0.9rem !important;
    }
    div.stButton > button {
        background: linear-gradient(135deg, #FFD700, #FFA500) !important;
        color: #141E30 !important;
        border-radius: 10px !important;
        font-weight: 600 !important;
        height: 48px !important;
        width: 100% !important;
    }
    </style>
    """, unsafe_allow_html=True)

    tab1, tab2 = st.tabs(["🔓 Login", "➕ Sign Up"])

    with tab1:
        st.title("🔐 Login")
        st.markdown("*Adaptive AI Coding Tutor*")

        username = st.text_input("👤 Username", placeholder="student / admin / guest")
        password = st.text_input("🔒 Password", type="password")

        if st.button("🚀 Login", use_container_width=True):
            users = load_users()
            if st.session_state.get("locked_out"):
                st.error("🔒 Account locked")
            elif username and password:
                if username in users and users[username] == hash_password(password):
                    st.session_state.authenticated = True
                    st.session_state.username = username
                    st.session_state.login_attempts = 0
                    st.rerun()
                else:
                    st.session_state.login_attempts += 1
                    if st.session_state.login_attempts >= 5:
                        st.session_state.locked_out = True
                    st.error("❌ Invalid credentials")
            else:
                st.warning("⚠️ Enter username & password")

        with st.expander("💡 Demo Accounts"):
            st.code("student / password123\nadmin / admin456\nguest / guest789")

    with tab2:
        st.title("➕ Sign Up")
        new_username = st.text_input("👤 New Username")
        new_password = st.text_input("🔒 Password (6+ chars)", type="password")
        
        if st.button("✅ Create Account", use_container_width=True):
            users = load_users()
            if new_username in users:
                st.error("❌ Username exists")
            elif len(new_password) < 6:
                st.error("❌ Password too short")
            else:
                users[new_username] = hash_password(new_password)
                save_users(users)
                st.success(f"✅ Account created for {new_username}!")
                st.info("Now login with your new account")

def profile_sidebar():
    """PERFECT SIDEBAR WITH WORKING PHOTO DISPLAY"""
    st.markdown("""
    <style>
    /* Clean sidebar styling */
    section[data-testid="sidebar"] div.element-container {
        background: rgba(20,30,48,0.95) !important;
        padding: 1.5rem !important;
        border-radius: 15px !important;
        border: 2px solid rgba(255,215,0,0.3) !important;
        margin: 1rem 0 !important;
    }
    .profile-pic {
        border-radius: 50% !important;
        border: 3px solid #FFD700 !important;
        width: 60px !important;
        height: 60px !important;
    }
    </style>
    """, unsafe_allow_html=True)

    if st.session_state.authenticated:
        st.markdown("### 👤 Profile")
        
        # PROFILE PHOTO DISPLAY - FIXED ✅
        col1, col2 = st.columns([1, 4])
        with col1:
            # Show uploaded photo OR default avatar
            if st.session_state.get("profile_photo"):
                # Convert bytes to image
                img = Image.open(io.BytesIO(st.session_state.profile_photo))
                st.image(img, width=60, output_type="show", use_container_width=False, clamp=True)
            else:
                st.markdown("""
                <div style='
                    width: 60px; height: 60px; 
                    background: linear-gradient(135deg, #FFD700, #FFA500);
                    border-radius: 50%; 
                    border: 3px solid #FFD700;
                    display: flex; align-items: center; justify-content: center;
                    font-size: 1.8rem;
                '>👨‍💻</div>
                """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"**{st.session_state.username}**")
            st.caption("Active Developer")

        # Live Stats
        col1, col2 = st.columns(2)
        with col1:
            st.metric("🔥 Streak", st.session_state.streak)
        with col2:
            st.metric("✅ Solved", st.session_state.correct)

        # Edit Profile
        if st.button("✏️ Edit Profile", key="edit_profile"):
            st.session_state.show_edit = True

        # Logout
        if st.button("🚪 Logout", key="logout"):
            st.session_state.authenticated = False
            st.session_state.username = None
            st.rerun()

        # EDIT PROFILE MODAL ✅
        if st.session_state.get("show_edit", False):
            with st.expander("📸 Edit Profile", expanded=True):
                uploaded_file = st.file_uploader("Choose profile photo", type=['jpg', 'jpeg', 'png'])
                
                if uploaded_file is not None:
                    image = Image.open(uploaded_file)
                    st.image(image, caption="Preview", width=150)
                    
                    if st.button("✅ Save Photo", key="save_photo"):
                        # FIXED: Store bytes directly
                        st.session_state.profile_photo = uploaded_file.read()
                        st.success("✅ Profile photo saved!")
                        st.rerun()
                
                if st.button("❌ Cancel Edit", key="cancel_edit"):
                    st.session_state.show_edit = False
                    st.rerun()

    else:
        st.info("🔐 Please login to see profile")

# Auto-save
import atexit
atexit.register(lambda: save_users(load_users()))
