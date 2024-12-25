from help.common.l import L

class K(L):
    def getProfilePic(self, user):
        return user.profilepic_user.filter(is_active=True).first()
    
    def getCoverPhoto(self, user):
        return user.coverphoto_user.filter(is_active=True).first()
    
    def getLink(self, level, user=None):
        link_obj = None
        if level == 'Landing': link_obj = {'name': 'Landing', 'link': '/'}
        elif level == 'Logout': link_obj = {'name': 'Logout', 'link': '/auth/logout/'}
        elif level == 'Profile': link_obj = {'name': 'Profile', 'link': f'/user/profile/{user.username}/'}
        elif level == 'Login': link_obj = {'name': 'Login', 'link': '/auth/login/'}
        elif level == 'Profile-Navbar': link_obj = {'name': user.first_name, 'link': f'/user/profile/{user.username}/', 'image': self.getProfilePic(user)}
        elif level == 'About': link_obj =  {'name': 'About', 'link': f'/user/about/'}
        return link_obj
            