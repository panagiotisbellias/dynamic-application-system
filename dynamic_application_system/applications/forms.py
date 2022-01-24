from django import forms

# dynamic 5
from .models import Application, ApplicationContent

# dynamic 2
class ApplicationForm(forms.ModelForm):
    your_name = forms.CharField(label='Your name', max_length=100,required=True)
    your_job = forms.CharField(label='Your job', max_length=400,required=True)
    headline = forms.CharField(label='Headline', max_length=200,required=True)
    # dynamic 4, 7
    #content_0 = forms.CharField(required=True)
    #content_1 = forms.CharField(required=True)
    #content_2 = forms.CharField(required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        contents = ApplicationContent.objects.filter(
            application = self.instance
        )
        for i in range(len(contents) + 1):
            field_name = 'content_%s' % (i,)
            self.fields[field_name] = forms.CharField(required=False)
            try:
                self.initial[field_name] = contents[i].interest
            except IndexError:
                self.initial[field_name] = ""
        # create an extra blank field
        field_name = 'content_%s' % (i + 1,)
        self.fields[field_name] = forms.CharField(required=False)

    '''
    def clean(self):
        contents = set()
        i = 0
        field_name = 'content_%s' % (i,)
        while self.cleaned_data.get(field_name):
            content = self.cleaned_data[field_name]
            if content in contents:
                self.add_error(field_name, 'Duplicate')
            else:
                contents.add(content)
            i += 1
            field_name = 'interest_%s' % (i,)
        self.cleaned_data["contents"] = contents
    '''

    # dynamic 6
    def save(self):
        Application = self.instance
        # TODO citizen details also
        Application.headline = self.cleaned_data["headline"]

        application.content_set.all().delete()
        # dynamic 8
        #for i in range(3):
        for content in self.cleaned_data["contents"]:
            # content = self.cleaned_data["content_{}".format(i)]
            ApplicationContent.objects.create(
                application=application, content=content
            )