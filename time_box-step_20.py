# === Stage 20: Добавь восстановление записей из архива ===
# Project: TimeBox
def restore_from_archive(archive_path, output_dir):
    import shutil, os, tarfile, zipfile, gzip
    if not os.path.isfile(archive_path):
        print(f"Архив не найден: {archive_path}")
        return False
    try:
        with open(archive_path, 'rb') as f:
            magic = f.read(2)
            if magic == b'PK':
                target = os.path.join(output_dir, 'timebox_archive.zip')
                with zipfile.ZipFile(f, 'r') as z:
                    shutil.copyfileobj(z, open(target, 'wb'))
                zipf = zipfile.ZipFile(target, 'r')
            elif magic in (b'BZ', b'GZ'):
                target = os.path.join(output_dir, 'timebox_archive.tar.gz')
                with tarfile.open(f, 'r:gz') as t:
                    shutil.copyfileobj(t, open(target, 'wb'))
                tarf = tarfile.open(target, 'r:gz')
            else:
                print("Неподдерживаемый формат архива")
                return False
        for member in zipf.namelist() if hasattr(zipf, 'namelist') else tarf.getmembers():
            out_path = os.path.join(output_dir, *member.split('/'))
            out_dir = os.path.dirname(out_path)
            if not os.path.exists(out_dir):
                os.makedirs(out_dir, exist_ok=True)
            with open(zipf.open(member).read() if hasattr(zipf, 'open') else tarf.extractfile(tarf.getnames().index(member)), 'rb') as src:
                dest = open(out_path, 'wb')
                shutil.copyfileobj(src, dest)
                dest.close()
        print(f"Архив восстановлен в {output_dir}")
        return True
    except Exception as e:
        print(f"Ошибка восстановления: {e}")
        return False
