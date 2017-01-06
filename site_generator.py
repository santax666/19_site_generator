import json
import os
from markdown import markdown as html_text
from jinja2 import Environment, FileSystemLoader
from collections import OrderedDict


def load_json_config(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r') as file_handler:
        return json.load(file_handler)


def save_to_html(data, file_name):
    out_dir = 'out/'
    out_file = '{0}{1}.html'.format(out_dir, file_name)
    os.makedirs(os.path.dirname(out_file), exist_ok=True)
    with open(out_file, "w") as filepath:
        filepath.write(data)


def generate_articles_pages(articles, env):
    in_dir = 'articles/'
    for article in articles:
        input_file = '{0}{1}'.format(in_dir, article['source'])
        input_str = open(input_file, 'r').read()
        article['text'] = html_text(input_str,
                                    extensions=['codehilite', 'fenced_code'])
        article_str = env.get_template('article.html').render(info=article)
        save_to_html(article_str, article['source'][:-3])


def generate_main_page(config, env):
    articles_dict = {}
    for article in config['articles']:
        articles_dict.setdefault(article['topic'], []).append(
            (article['title'], article['source'][:-3] + '.html',))
    for topic in config['topics']:
        articles_dict[topic['title']] = articles_dict.pop(topic['slug'])
    art_sort = OrderedDict(sorted(articles_dict.items(), key=lambda x: x[0]))
    main_str = env.get_template('main.html').render(info=art_sort)
    save_to_html(main_str, 'index')


if __name__ == '__main__':
    config = load_json_config('config.json')
    articles = config['articles']
    j2_env = Environment(loader=FileSystemLoader('templates/bootstrap'),
                         trim_blocks=True)
    generate_articles_pages(articles, j2_env)
    generate_main_page(config, j2_env)
