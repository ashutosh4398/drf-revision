from .permissions import isStaffEditiorPermission
from .authentication import TokenAuthentication
from rest_framework.authentication import SessionAuthentication

class ProdcutEditorPermissionMixin():
    permission_classes = [isStaffEditiorPermission]
    authentication_classes = [TokenAuthentication, SessionAuthentication]