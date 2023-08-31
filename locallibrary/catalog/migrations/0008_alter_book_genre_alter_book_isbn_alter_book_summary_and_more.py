# Generated by Django 4.2.4 on 2023-08-30 04:17

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_remove_bookinstance_borrower_alter_bookinstance_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.ManyToManyField(help_text='Chọn thể loại cho cuốn sách này', to='catalog.genre'),
        ),
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.CharField(help_text='13 ký tự <a href="https://www.isbn-international.org/content/what-isbn">số IBSN</a>', max_length=13, unique=True, verbose_name='ISBN'),
        ),
        migrations.AlterField(
            model_name='book',
            name='summary',
            field=models.TextField(help_text='Nhập mô tả ngắn gọn cho sách', max_length=1000),
        ),
        migrations.AlterField(
            model_name='bookinstance',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, help_text='ID duy nhất cho cuốn sách cụ thể này trên toàn bộ thư viện', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bookinstance',
            name='status',
            field=models.CharField(blank=True, choices=[('m', 'Bảo trì'), ('o', 'Đang cho mượn'), ('a', 'Có sẵn'), ('r', 'Dành riêng')], default='m', help_text='Sách có sẵn', max_length=1),
        ),
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(help_text='Nhập thể loại sách (ví dụ Khoa học viễn tưởng)', max_length=200),
        ),
    ]