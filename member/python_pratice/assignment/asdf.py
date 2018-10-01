from member.models import AccountManager

if __name__ == '__main__':
    AccountManager.create_superuser(username='sky5367', email='KimSoungRyoul@gmail.com', name='soungryoul',
                                    password='1234')
