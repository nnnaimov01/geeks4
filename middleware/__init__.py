from loader import dp
from .channel import ChannelMiddleware

if __name__ == "middleware":
    dp.middleware.setup(ChannelMiddleware())