from notepad.serializer import UploadFilesSerializer, NotesSerializer
from notepad.services.notes_limit import NotesLimitService


class UploadService:
    def __init__(self, request_user, code, user=None, delete_after_viewing=False, delete_time=None, language="python", style="native"):
        self.data = {
            "code": str(code),
            "user": request_user.pk,
            "delete_after_viewing": delete_after_viewing,
            "delete_time": delete_time,
            "language": language,
            "style": style,
        }
        self.request_user = request_user

    @classmethod
    def from_file(cls, file, request_user):
        code = file.read().decode("utf-8")
        return cls(request_user, code)

    def __call__(self):
        NotesLimitService(self.request_user)()
        
        serializer = NotesSerializer(data=self.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()
        return serializer.instance
