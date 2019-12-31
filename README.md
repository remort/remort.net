# remort.net

Захотел сделать маленький статический сайт, собираемый из markdown документов.

Написал свой сборщик статических html на python т.к. не осилил
пробегание по .md файлам для создания меню сайта на nodejs/gulp.

    virtualenv -p python3.7 venv
    pip install -r requirements.txt
    source venv/bin/activate
    python build.py
