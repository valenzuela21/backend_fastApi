from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify(plain, hashed):
    return pwd_context.verify(plain, hashed)


def get_hash(value):
    return pwd_context.hash(value)