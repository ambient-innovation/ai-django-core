# Antivirus for Django

Uses AVG and clamAV to scan uploads for malware.


## Setup

### AVG
```
    rm /opt/avg/av/var/run/avgd.pid
    avgctl --start
```

### clamAV
```
    apt-get install clamav-daemon
    freshclam
    /etc/init.d/clamav-daemon start
```


## Usage
There're multiple ways, thou shalt use just one!

### Storage
Either you check every upload by setting a custom `FileSystemStorage`:

```
    upload_storage = antivirus.AVFileSystemStorage(location=settings.FILES_ROOT, base_url=settings.FILES_URL)
```

### ModelField
Or you set a modified `ModelField` to add a validator to `ModelForm`s:

```
    dokument = antivirus.AVProtectedFileField(_(u"Angebot"), upload_to=upload_location, storage=upload_storage, null=True)
```

### Serializer
Maybe later...


### Manual

```
    try:
        wert_object.save()
    except AVException:
        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
```
