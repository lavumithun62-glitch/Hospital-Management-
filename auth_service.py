from app.models.user import User
from app.utils.hashing import hash_password, verify_password
from app.utils.jwt_handler import create_access_token

def register_user(db, user):
    hashed = hash_password(user.password)

    new_user = User(
        name=user.name,
        email=user.email,
        password=hashed,
        role=user.role
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

def login_user(db, email, password):
    user = db.query(User).filter(User.email == email).first()

    if not user:
        return None

    if not verify_password(password, user.password):
        return None

    return create_access_token({
        "sub": user.email,
        "role": user.role
    })
