from notepad.serializer import UploadFilesSerializer, NotesSerializer


class UploadService:
    def __init__(self, request_user, code, user, delete_after_viewing=False, delete_time=None, language="python", style="native"):
        self.data = {
            "code": str(code),
            "user": request_user,
            "delete_after_viewing": delete_after_viewing,
            "delete_time": delete_time,
            "language": language,
            "style": style,

        }

    @classmethod
    def from_file(cls, file):
        code = file.read().decode("utf-8")
        return cls(code)

    def __call__(self):
        serializer = NotesSerializer(data=self.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()
        return serializer.instance
