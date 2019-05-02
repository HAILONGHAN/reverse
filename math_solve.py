#!/usr/bin/python
import numpy as np
aim = [35165,34313,38133,36833,35394,31297,33481,33131,31266,36449,31147,31201,32076,34753,35719,34279,37124,33322,33642,30716,29382,39319,34920,32949,34794,35842,35960,31636,34383,32698]
box = ["qargczetzutyoildyeqqfxhozkmjgt","hsugzdksumrzfsjbctyietafiukhxj","yuvhxsavytvwibnxgniztappgowsaa","nwdmczuevvhjigkczgiiwsxsotoiwu","tedzxstaqvsbdeqhwkgmgqwhujsomv","jzqthhuebkltmrqdbhvzggpmyoqneb","xjqpvhwrbgqbvhaicpnlwxpsaugxpc","xuoypiawmsebttpolykjcdffwabxaz","kgrftmbvteqhveithvyxxebttfdhfn","fadyzlwklpvujckwnxiorenluzwjll","hgcnjougkjysicnhuxqfuqeoekeyjt","mybmfvmxswldiuunbcnimpikvaking","fveyiajylcvntzuhexaehgqstytkbg","byrigtbszafusdxnxxpmdrpnnhzfxb","tdntvjrojknstuxlgjukbvmhtgwgrl","phdjixkqbjnglzwupuxwtxevkjural","ivjzzgqowrzultkbhimukjmpbrycjr","krzhtlutxqnprffuwljlyhkdpfdecf","mzcybnmryrficpiulgwmnjkhfnsrjp","vmptmbdrufvpxohlijubendwgfcpby","qdwkoegydgggzxhpmginszaihitbcu","vofwzqpuejwguykxewhdjnmunkpyxl","ukmxzmrjgghuaipnpbaomyxfnvfphz","hcjgmwhaagsxenurxomzlshyvzfkms","ondoalzxwqhedwzlesawxvmkdtphsg","juiuynqikmxpqkbgwtrzdhwobkwzje","fpxwomkyznykfesigdtykoqtcheqro","bfgayguopwbdbvlnwlbjpuyykkukrm","fhvfwkcgrhgrnwinlnvvstxoeproyf","tlshbyzyewenvqaysvgthdujbgckbx"]
bim = []

aim = [i for i in aim]

for st in box:
  tmp = list(st)
  tmp2 = [ord(i)-97 for i in tmp]
  bim.append(tmp2)

print bim
print aim

a = np.array(bim)
b= np.array(aim)

c= np.linalg.solve(a,b)

c = list(c)
m=[int(round(i)) for i in c]
m = [chr(j) for j in m]
print ''.join(m)

