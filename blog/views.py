from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from blog.models import Blog


class BlogListView(ListView):
    """Отображает список блоговых записей."""

    model = Blog
    template_name = "blog/blog_list.html"
    context_object_name = "blogs"

    def get_queryset(self):
        """Возвращает только опубликованные записи."""
        return Blog.objects.filter(is_published=True)


class BlogDetailView(DetailView):
    """Отображает блоговую запись."""

    model = Blog
    template_name = "blog/blog_detail.html"
    context_object_name = "blog"

    def get_object(self, queryset=None):
        """Получает запись и увеличивает счетчик просмотров."""
        blog = super().get_object(queryset)
        blog.views_count += 1
        blog.save()
        return blog


class BlogCreateView(CreateView):
    """Создает блоговую запись."""

    model = Blog
    fields = ("title", "content", "preview", "is_published")
    template_name = "blog/blog_form.html"
    success_url = "/blogs/"


class BlogUpdateView(UpdateView):
    """Редактирует блоговую запись."""

    model = Blog
    fields = ("title", "content", "preview", "is_published")
    template_name = "blog/blog_form.html"
    success_url = "/blogs/{id}/"


class BlogDeleteView(DeleteView):
    """Удаляет блоговую запись."""

    model = Blog
    template_name = "blog/blog_confirm_delete.html"
    success_url = "/blogs/"
