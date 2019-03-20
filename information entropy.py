from math import *
import random
alpha = 'abcdefghijklmnopqrstuvwxyz,. '

def entropy(string,base=255):
    '''
    Non-normalized entropy
    '''
    sample_space = len(string)
    count = []
    exclusion = []
    for i in string:
        if i not in exclusion:
            exclusion.append(i)
            count.append( string.count(i))
    P = 0
    for i in count:
        P += - log(i/(sample_space**sample_space), base)
    return P

def shanonE(string):
    '''
    Shanon Entropy of a word.
    '''
    sample_space = len(string)
    count = []
    exclusion = []
    for i in string:
        if i not in exclusion:
            exclusion.append(i)
            count.append( string.count(i))
    P = 0
    for i in count:
        prob = i/(sample_space)
        P += - log(prob, 2) * (prob)
    return P

def test():
    E = []
    S = []
    for i in range(1000):
        string = ''.join([random.choice(alpha) for i in range(random.randint(1,8))])
        S.append(string)
        E.append(entropy(string))    
    print(log(256,256))
    print( max(E), S[E.index(max(E))])
    print( min(E), S[E.index(min(E))])

    import matplotlib.pyplot as plt

    plt.plot(S[:7],E[:7])
    plt.show()

def quran_plot():
    import matplotlib.pyplot as plt

    with open('quran-simple-clean.txt', encoding='utf8') as afile:
        data = afile.readlines()
    for i in data:
        if i.startswith('#'):
            data.remove(i)
    D = []
    for line in data:
        D.append(line.split('|')[-1].replace('\n',''))
    S = []
    for i in D:
        [S.append(j) for j in i.split(' ')]

    E = []
    for i in S:
        E.append(shanonE(i))
    print( sum(E)/len(E) )
    plt.xlabel('Line Number')
    plt.ylabel('Shanon Entropy')
    plt.plot(E)
    plt.show()

def text_entropy(text):
    import matplotlib.pyplot as plt
    text = text.split('\n')
    words = []
    for line in text:
        words += line.split(' ')
    E = []
    for line in words:
        
        if len(line) != 0:
            E.append(shanonE(line))
    print(sum(E)/len(E))
    plt.plot(E)
    plt.show()

a = '''The Territorial Force was a part-time volunteer component of the British Army, created in 1908 to augment British land forces without resorting to conscription. The new organisation consolidated the 19th-century Volunteer Force and yeomanry into a unified auxiliary, commanded by the War Office and administered by local County Territorial Associations. The Territorial Force was designed to reinforce the regular army in expeditionary operations abroad, but because of political opposition it was assigned to home defence. Members were liable for service anywhere in the UK and could not be compelled to serve overseas. In the first two months of the First World War, territorials volunteered for foreign service in significant numbers, allowing territorial units to be deployed abroad. They saw their first action on the Western Front during the initial German offensive of 1914, and the force filled the gap between the near destruction of the regular army that year and the arrival of the New Army in 1915. Territorial units were deployed to Gallipoli in 1915 and, following the failure of that campaign, provided the bulk of the British contribution to allied forces in the Sinai and Palestine Campaign. By the war's end, the Territorial Force had fielded twenty-three infantry divisions and two mounted divisions on foreign soil. It was demobilised after the war and reconstituted in 1921 as the Territorial Army.

The force experienced problems throughout its existence. On establishment, fewer than 40 per cent of the men in the previous auxiliary institutions transferred into it, and it was consistently under strength until the outbreak of the First World War. It was not considered to be an effective military force by the regular army and was denigrated by the proponents of conscription. Lord Kitchener chose to concentrate the Territorial Force on home defence and raise the New Army to reinforce the British Expeditionary Force (BEF) in France, a decision which disappointed the territorials. The need to replace heavy losses suffered by the BEF before the New Army was ready forced Kitchener to deploy territorial units overseas, compromising the force's ability to defend the homeland. To replace foreign-service units, the Territorial Force was doubled in size by creating a second line which mirrored the organisation of the original, first-line units. Second-line units assumed responsibility for home defence and provided replacement drafts to the first line. The second line competed with the New Army for limited resources, and was poorly equipped and armed. The provision of replacements to the first line compromised the second-line's home defence capabilities until a third line was raised to take over responsibility for territorial recruitment and training. The second line's duties were further complicated by the expectation, later confirmed, that it too would be deployed overseas.

Territorial units were initially deployed overseas to free up regular units from non-combat duties. On the Western Front, individual battalions were attached to regular army formations and sent into action, and the territorials were credited with playing a key role in stopping the German offensive. The first complete territorial division to be deployed to a combat zone arrived in France in March 1915. Territorial divisions began participating in offensive operations on the Western Front from June 1915 and at Gallipoli later that year. Because of the way it was constituted and recruited, the Territorial Force possessed an identity that was distinct from the regular army and the New Army. This became increasingly diluted as heavy casualties were replaced with conscripted recruits following the introduction of compulsory service in early 1916. The Territorial Force was further eroded as a separate institution when County Territorial Associations were relieved of most of their administrative responsibilities. By the war's end, there was little to distinguish between regular, territorial and New Army formations. 
'''

#text_entropy(a)
#quran_plot()
