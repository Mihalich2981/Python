alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
messages = list('vujgvmCfb tj ufscfu ouib z/vhm jdjuFyqm jt fscfuu uibo jdju/jnqm fTjnqm tj scfuuf ibou fy/dpnqm '
                'yDpnqmf jt cfuufs boui dbufe/dpnqmj uGmb tj fuufsc ouib oftufe/ bstfTq jt uufscf uibo otf/ef '
                'uzSfbebcjmj vout/dp djbmTqf dbtft (ubsfo djbmtqf hifopv up csfbl ifu t/svmf ipvhiBmu zqsbdujdbmju '
                'fbutc uz/qvsj Fsspst tipvme wfsof qbtt foumz/tjm omfttV mjdjumzfyq odfe/tjmf Jo fui dfgb pg '
                'hvjuz-bncj gvtfsf fui ubujpoufnq up ftt/hv Uifsf vmetip fc pof.. boe sbcmzqsfgf zpom pof pvt..pcwj '
                'xbz pu pe ju/ Bmuipvhi uibu bzx bzn puo cf wjpvtpc bu jstug ttvomf sfzpv( i/Evud xOp tj scfuuf ibou '
                '/ofwfs uipvhiBm fsofw jt fopgu cfuufs boui iu++sjh x/op gJ ifu nfoubujpojnqmf tj eibs pu mbjo-fyq '
                'tju( b bec /jefb Jg fui foubujpojnqmfn jt fbtz up bjo-fyqm ju znb cf b hppe jefb/ bnftqbdftO bsf pof '
                'ipoljoh sfbuh efbj .. fu(tm pe psfn gp tf"uip '.split())
code_messages = []
num = 0
for i_line in messages:
    lst = [(alpha[(alpha.index(sym) - 1) % len(alpha)] if sym.isalpha() else sym) for sym in i_line]
    new_lst = [i_sym for i_sym in lst]
    var_list = []
    for _ in range(num + 3):
        var_list.append(new_lst[-1])
        for i in range(len(new_lst) - 1):
            if new_lst[i] == '.':
                new_lst[i] = '-'
            if new_lst[i] == '/':
                new_lst[i] = '.\n'
                num += 1
            if new_lst[i] == '(':
                new_lst[i] = "'"
            if new_lst[i] == '+':
                new_lst[i] = '*'
            if new_lst[i] == '"':
                new_lst[i] = '!'
            var_list.append(new_lst[i])
        new_lst = var_list
        var_list = []
    line = ''.join(new_lst)
    code_messages.append(line)
print('\n         Дзен Питона:\n\n', ' '.join(code_messages))


# зачет!
