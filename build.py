import base64
from pathlib import Path, PosixPath
from typing import List, Tuple

from jinja2 import Template
from markdown import Markdown
from scss.compiler import compile_string

md: Markdown = Markdown(extensions=['meta'])
template_path: PosixPath = Path('src/template.html')
build_dir: PosixPath = Path('build')
favicon_path: PosixPath = Path('src/favicon.png')
sass_file_path: PosixPath = Path('src/style.sass')


def get_menu_items() -> List[Tuple[str, str, int]]:
    menu_items: List[Tuple[str, str, int]] = list()
    file: PosixPath
    for file in Path('pages').glob('*.md'):
        with open(file, 'rt') as content:
            md.convert(content.read())
            title: str = md.Meta['title'].pop()
            order: int = int(md.Meta['order'].pop())
            menu_items.append(
                (Path(Path(content.name).stem).with_suffix('.html').as_posix(), title, order)
            )
    return sorted(menu_items, key=lambda x: x[2])


def clean_build_dir():
    if any((build_dir.is_file(), build_dir.is_symlink())):
        build_dir.unlink()

    path: PosixPath
    build_dir.mkdir(exist_ok=True)
    for path in build_dir.iterdir():
        path.unlink()


def encode_favicon() -> str:
    with favicon_path.open('rb') as content:
        return base64.b64encode(content.read()).decode('ascii')


def render_pages(menu_items: List[Tuple[str, str, int]]):
    page_tmpl: Template = Template(template_path.open().read())
    favicon: str = encode_favicon()
    file: PosixPath
    for file in Path('pages').glob('*.md'):
        with open(file, 'rt') as content:
            html_filename: PosixPath = build_dir.joinpath('dummy.filename').with_name(
                Path(Path(content.name).stem).with_suffix('.html').as_posix()
            )
            built_content: str = page_tmpl.render(
                page_content=md.convert(content.read()),
                meta=md.Meta,
                menu_items=menu_items,
                favicon=favicon,
            )

        with html_filename.open('wt') as file:
            file.write(built_content)


def compile_css():
    with sass_file_path.open('rt') as sass_content:
        css_content: str = compile_string(sass_content.read(), output_style='compressed')
    css_filename: PosixPath = build_dir.joinpath('dummy.filename').with_name(
        Path(sass_file_path.stem).with_suffix('.css').as_posix()
    )

    with css_filename.open('wt') as file:
        file.write(css_content)


if __name__ == '__main__':
    menu: List[Tuple[str, str, int]] = get_menu_items()
    clean_build_dir()
    render_pages(menu)
    compile_css()
