
## Language Turkish and English

```markdown
# Proje Açıklaması
Bu proje, `django-tenants` kullanarak çoklu kiracı sistemi üzerinde çalışmaktadır. Veriler, şema düzeyinde izolasyon sağlanarak yönetilmektedir. Ancak, her şema için farklı bir domain olması bazı problemlere yol açmaktadır.

Bu problemi çözmek için `django-tenants` kütüphanesinde birkaç değişiklik yapmış bulunmaktayım. Öncelikle, `request.user` ile kiracı modeli arasında bir `ForeignKey` oluşturulmuştur. Ardından, `django-tenants`'ın `middleware`'ini genişleterek, `request.user`'dan bağlı olduğu kiracıyı alıp mevcut kiracı olarak atamış bulunmaktayım.

Bu sayede, tek bir URL üzerinden şema düzeyinde izolasyon sağlanabilmektedir.

# Django Projesi Kurulumu

Bu belge, Django projesinin nasıl kurulacağını adım adım anlatmaktadır.

## Adım 1: Projenin İndirilmesi ve Ayar Dosyalarının Hazırlanması

Django projesini indirin ve `.env`, `local.py`, `local_test.py` dosyalarını ekleyin. `example` dosyasında verilen bilgileri bu dosyalara ekleyerek güncelleyin. `.env` dosyasına veritabanı bilgilerinizi yazın. Bu projede **PostgreSQL** kullanılmıştır.

## Adım 2: Gerekli Kütüphanelerin Kurulumu

Gerekli kütüphaneleri aşağıdaki komut ile Python sanal ortamınıza kurun:

```bash
pip install -r requirements.txt
```

## Adım 3: Veritabanı Ayarlarının Yapılması

Aşağıdaki komutları sırasıyla çalıştırın:

```bash
python manage.py makemigrations
python manage.py migrate
```

## Adım 4: Tenant Ayarlarının Yapılması

Python shell'i açın (python manage.py shell) ve aşağıdaki komutları sırasıyla çalıştırın:
```python
from my_project.apps.tenant.models import Organization, Domain
tenant = Organization(schema_name="public",name="public")
tenant.save()
domain = Domain(domain="localhost",tenant=tenant,is_primary=True)
domain.save()
tenant = Organization(schema_name="burak",name="burak")
tenant.save()
domain = Domain(domain="burak.localhost",tenant=tenant,is_primary=True)
domain.save()
!
```
![tenant_config](https://i.hizliresim.com/5vx0p4q.png)

Shell'i kapatın ve aşağıdaki komutu çalıştırın:

```bash
python manage.py create_tenant_superuser
```

Bu komut, hangi şema için yönetici oluşturmak istediğinizi soracaktır. Bu projede "burak" şemasını seçin ve yönetici hesabınızı oluşturun.

## Adım 5: Kullanıcı Ayarlarının Yapılması

Python shell'i tekrar açın ve aşağıdaki komutları sırasıyla çalıştırın:

```python
from my_project.apps.tenant.models import Organization
from my_project.apps.accounts.models import User
org= Organization.objects.last()
user = User.objects.last()
user.organization = org
user.save()
```
![shell](https://i.hizliresim.com/7fp5tzb.png)
Shell'den çıkın ve Django projenizi başlatın:

```bash
python manage.py runserver
```
```

Bu yapıyı kullanarak, projenizin kurulum sürecini adım adım takip edebilirsiniz.