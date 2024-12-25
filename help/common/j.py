from help.common.k import K

class J(K):
    def getNavbar(self, user, navbar):
        navbar_obj = {
            'left_side': {'simple': [], 'profile': []},
            'right_side': {'simple': [], 'profile': []}
        }
        if navbar == 1:
            # profile
            navbar_obj['left_side']['simple'].append(self.getLink('Landing'))
            navbar_obj['right_side']['simple'].append(self.getLink('Logout'))
            navbar_obj['right_side']['profile'].append(self.getLink('Profile-Navbar', user))
        elif navbar == 2:
            # landing
            if user.is_authenticated:
                navbar_obj['left_side']['simple'].append(self.getLink('Profile', user))
                navbar_obj['right_side']['simple'].append(self.getLink('Logout'))
                navbar_obj['right_side']['profile'].append(self.getLink('Profile-Navbar', user))
            else:
                navbar_obj['left_side']['simple'].append(self.getLink('About'))
                navbar_obj['right_side']['simple'].append(self.getLink('Login'))
        elif navbar == 3:
            # login
            navbar_obj['left_side']['simple'].append(self.getLink('Landing'))
            navbar_obj['left_side']['simple'].append(self.getLink('About'))

        return navbar_obj