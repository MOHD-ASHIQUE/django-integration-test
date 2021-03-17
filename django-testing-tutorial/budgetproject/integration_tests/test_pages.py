from selenium import webdriver
from budget.models import Project,Category
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
import time
import pytest
from mixer.backend.django import mixer

@pytest.mark.django_db
def test_projects_are_empty(setup):
    Project.objects.filter(id=1).delete()
    #url = reverse('list')
    setup.get("http://127.0.0.1:8000/")
    time.sleep(1)
    try:
        alert = setup.find_element_by_class_name('noproject-wrapper')
        assert(
            alert.find_element_by_tag_name('h3').text,
            'Sorry, you don\'t have any projects, yet.'
        )

        time.sleep(2)
        add_url= setup.current_url + reverse('add')

        setup.find_element_by_tag_name('a').click()

        time.sleep(2)
        
        assert(
            add_url,
            setup.current_url,
        )

        time.sleep(2)
            
        # project1 = Project.objects.create(
        #     name='ashique',
        #     budget=50000,
        #     #category='sales'
        # )
        project1 = mixer.blend('budget.Project',name='ashique',budget=5000)

        setup.find_element_by_id('id_name').send_keys('ashique')
        setup.find_element_by_id('id_budget').send_keys(5000)
        setup.find_element_by_id('categoryInput').send_keys('sales')

        time.sleep(2)

        detail_url = setup.current_url + reverse('detail',args=[project1.slug])
        setup.find_element_by_tag_name('button').click()

        time.sleep(2)
        assert(
            detail_url,
            setup.current_url,
        )
        time.sleep(2)

        setup.find_element_by_tag_name('button').click()

        setup.find_element_by_id('title').send_keys('first_transaction')
        setup.find_element_by_id('amount').send_keys(100)

        time.sleep(2)
    except:
        assert("project not empty")

@pytest.mark.django_db
def test_project_not_empty(setup):

    # project1 = Project.objects.create(
    #     name='ashique',
    #     budget=5000
    # )
    # category1 = Category.objects.create(
    #     project = project1,
    #     name='sales'
    # )
    project1 = mixer.blend('budget.Project',name='ashique',budget=5000)
    categorr1 = mixer.blend('budget.Category',project=project1,name='sales')
    setup.get("http://127.0.0.1:8000/")
    
    time.sleep(2)
        
    detail_url =  setup.current_url + reverse('detail',args=[project1.slug])
    setup.find_element_by_tag_name('a').click()

    time.sleep(2)

        
    assert(
        setup.current_url,
        detail_url
    )
    time.sleep(2)

    setup.find_element_by_tag_name('button').click()

    setup.find_element_by_id('title').send_keys('first_transaction')
    setup.find_element_by_id('amount').send_keys(100)
    
    time.sleep(2)

    setup.find_element_by_tag_name('button').click()
    time.sleep(2)