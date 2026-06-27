from django.db import models



class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=11)
    address = models.TextField()
    status = models.CharField(
        max_length=100,
        choices=[
            ("new", "new"),
            ("contacted", "contacted"),
            ("customer", "customer"),
        ],
         default="new",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name



class Note(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="notes")
    note = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'note for : {self.customer.name}'