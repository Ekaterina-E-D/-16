class cassa(object):
    sum=14540

    def top_up(self, pokup):
        self.pokup = pokup
        pokup += cassa.sum
        return f"в кассе {pokup}"
    
    def count_1000(self):
        print(cassa.sum//1000)

    def take_away(self,x):
        if x <= self.sum:
            self.sum -= x
        else:
            return f"не достаточно денег"
r=cassa()
print(r.top_up(165))