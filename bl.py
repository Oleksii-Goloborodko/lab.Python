import numpy as np

class Bl:
    def All_bl(self):
        arrayR = np.array(self.logic_list)
        arrayR = arrayR.reshape(3, 3)
        buf_num = [0, 1, 2]
        for i in buf_num:
            if arrayR[i][0] != 0 and arrayR[i][1] != 0 and arrayR[i][2] != 0:
                if arrayR[i][0] == arrayR[i][1] and arrayR[i][1] == arrayR[i][2]:
                    return arrayR[i][0]
            elif arrayR[0][i] != 0 and arrayR[1][i] != 0 and arrayR[2][i] != 0:
                if arrayR[0][i] == arrayR[1][i] and arrayR[1][i] == arrayR[2][i]:
                    print("s")
                    return arrayR[0][i]
            elif arrayR[0][0] != 0 and arrayR[1][1] != 0 and arrayR[2][2] != 0:
                if arrayR[0][0] == arrayR[1][1] and arrayR[1][1] == arrayR[2][2]:
                    return arrayR[0][0]
            elif arrayR[0][2] != 0 and arrayR[1][1] != 0 and arrayR[2][0] != 0:
                if arrayR[0][2] == arrayR[1][1] and arrayR[1][1] == arrayR[2][0]:
                    return arrayR[0][2]
        return False

