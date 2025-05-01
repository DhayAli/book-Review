from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedDefaultRouter

from .views import UserViewSet, BookViewSet, ReviewViewSet

router = DefaultRouter()
router.register(r'auth', UserViewSet, basename='auth')
router.register(r'books', BookViewSet, basename='books')

# Nested Router للريفيوز الخاصة بكتاب معين
books_router = NestedDefaultRouter(router, r'books', lookup='book')
books_router.register(r'reviews', ReviewViewSet, basename='book-reviews')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(books_router.urls)),  # إضافة المسار المتداخل
]
