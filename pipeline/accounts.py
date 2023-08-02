from typing import Callable
from dataclasses import dataclass

from secret_manager_service import get_secret

@dataclass
class Account:
    id: str
    refresh_token: Callable[[], str]

ACCOUNTS = [
    Account("176151959", lambda: get_secret('BING_REFRESH_TOKEN_176151959')),
    Account("176151963", lambda: get_secret('BING_REFRESH_TOKEN_176151963')),
]
