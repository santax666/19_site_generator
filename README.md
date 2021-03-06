
# Site Generator

Данный скрипт:
* считывает конфигурационный файл [config.json][] со списком статей, написаных на [языке разметки Markdown][];
* выполняет конвертацию вышеуказанных статей в HTML формат с последующим сохранением в отдельной директории;
* дополнительно формируется индексная страница со списком всех статей и ссылками на них.

Ознакомиться со сгенерированными страницами Вы можете на [Демо-сайте][].

## Запуск

Введите в терминале:

    python3 site_generator.py

## Зависимости

Скрипт написан на языке Python 3, поэтому требует его наличия.

Для преобразования статей из MD- в HTML- формат должен быть установлен модуль [markdown][].

Для формирования HTML-страниц должен быть установлен модуль [jinja2][].

Конфигурационный файл должен располагаться в одной директории со скриптом!

## Поддержка

Если у вас возникли сложности или вопросы по использованию скрипта, создайте 
[обсуждение][] в данном репозитории или напишите на электронную почту 
<IvanovVI87@gmail.com>.

## Документация

Документацию к модулю markdown можно получить по [ссылке1][].

Документацию к модулю jinja2 можно получить по [ссылке2][].

[Демо-сайте]: https://santax666.github.io/19/
[config.json]: ./config.json
[языке разметки Markdown]: https://ru.wikipedia.org/wiki/Markdown
[markdown]: https://pypi.python.org/pypi/Markdown
[jinja2]: https://pypi.python.org/pypi/Jinja2
[обсуждение]: https://github.com/santax666/19_site_generator/issues
[ссылке1]: http://pythonhosted.org/Markdown/
[ссылке2]: http://jinja.pocoo.org/2/documentation/
