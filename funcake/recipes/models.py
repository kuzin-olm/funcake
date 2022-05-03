from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils import timezone
from PIL import Image


User = get_user_model()


def recipe_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT / recipe_<pk>/<filename>
    return 'recipe_{0}/{1}'.format(instance.pk, filename)


class AutoDateTimeField(models.DateTimeField):
    def pre_save(self, model_instance, add):
        return timezone.now()


class Recipe(models.Model):

    title = models.CharField("Название", max_length=250, unique=True)
    preview = models.CharField("Краткое описание", max_length=250)
    description = models.TextField("Описание")
    text = models.TextField("Текст рецепта")
    created_at = models.DateField("Дата создания", auto_now_add=True)
    updated_at = AutoDateTimeField("Дата изменения", default=timezone.now)
    is_visible = models.BooleanField("Видимость", default=False)
    img_prew = models.ImageField(verbose_name="Фото превью", upload_to=recipe_directory_path, blank=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("recipes:detail", kwargs={"pk": self.pk})

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # если есть загруженная картинка
        # потом лучше перенести в форму
        if self.img_prew:
            img = Image.open(self.img_prew.path)
            width, height = img.size

            is_resizing = False
            if width > 300:
                w = width/300
                width /= w
                height /= w
                is_resizing = True

            if height > 300:
                h = height / 300
                height /= h
                width /= h
                is_resizing = True

            if is_resizing:
                img.thumbnail((width, height))
                img.save(self.img_prew.path)
                img.close()
