from comments import forms



class TestPostForm:
    def test_form(self):
        form = forms.PostForm(data={})
        assert form.is_valid() is False,'Should be invalid if no data is given'
       
        form = forms.PostForm(data={'content': 'Hello'})
        assert form.is_valid() is False,'Should be invalid if body text is less than 10 characters'
        assert 'content' in form.errors, 'Should return field error for `content`'
        data = {'content': 'Hello !'}
        form = forms.PostForm(data=data)
        assert form.is_valid() is True, 'Should be valid when data is given'