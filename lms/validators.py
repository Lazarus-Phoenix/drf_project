import re

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class ExternalLinksValidator:
    def __init__(self, allowed_domains=None, field=None):
        if allowed_domains is None:
            allowed_domains = ["youtube.com"]
        self.allowed_domains = allowed_domains
        self.field = field  # Добавлен аргумент field

    def __call__(self, value):
        if not value:  # Пропускаем пустые значения
            return
        url_pattern = r"(https?://[^\\s]+)"
        urls = re.findall(url_pattern, value)

        for url in urls:
            if not any(domain in url for domain in self.allowed_domains):
                raise ValidationError(
                    _(
                        "Ссылка на сторонний ресурс обнаружена в поле %(field)s: %(url)s"
                    ),
                    params={
                        "field": self.field,
                        "url": url,
                    },  # Используем field для вывода в ошибке
                )
