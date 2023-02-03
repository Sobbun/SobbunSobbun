# Database

## DB Migrations
DB 모델링의 변경이 있을시, DB의 스키마를 고쳐줘야합니다. Django는 자체적으로 이 기능을 가지고 있습니다. 단 큰 변화일시 직접 고치는 코드를 작성하는등의 추가 작업이 필요합니다. 큰 변경은 최대한 초기에만 합시다.

```shell
> python manage.py makemigrations 
Migrations for 'app': ....
> python manage.py migrate
Operations to perform: ...
```

## DB Reset

아직 heavy-development 단계, DB 재 모델링 상태입니다. 이 경우 계속 수정시 migrations 가 엄청나게 복잡해지며, 이걸 방지하기 위해 주기적 Migration Reset을 하고있습니다.


```console
# # 현재 마이그레이션 조회
> python manage.py makemigrations
No changes detected

# #  No changes detected 상태일시에만 진행.
# # 현재 migrations 조회
> python manage.py showmigrations
...
common
 [X] 0001_initial
 [X] 0002_area_trustlevel_event_locationverification
...

# # 특정 앱을 골라서 진행. `common`의 경우
# # --fake 옵션으로 실제로 진행하지 않고 롤백 한 것처럼 기록함.
> python manage.py migrate --fake common zero
...
common
 [ ] 0001_initial
 [ ] 0002_area_trustlevel_event_locationverification
...

# # migrations 확인. 
> python manage.py showmigrations

# # 해당 app의 migrations 폴더 내부 삭제. __init__.py를 제외한 모든 *.py 파일 및 __pycache__ 폴더 삭제.
# # 아래의 명령어는 리눅스 명령어. 직접 삭제해도 상관 없음.
$ find . -path "common/migrations/*.py" -not -name "__init__.py" -delete
$ find . -path "common/migrations/*.pyc"  -delete

# # makemigrations
> python manage.py makemigrations

# # migrate, --fake-initial 옵션으로 한것처럼 보이게 하고 정작 안함.
> python manage.py migrate --fake-initial
```