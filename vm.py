#!/usr/bin/python

import sys

def main():
    """
    VM body
    """
    
    class C(object):
        var_map = {}
        jmp_map = {}
        cursor = None
        src = []
        cmds = []
    
    # Phase one: load file to SRC
    try:
        src_file = sys.argv[1]
        src = [line.strip() for line in open(src_file)]
    except IndexError:
        print 'Error: You have to define source file name'
        return False
    except IOError:
        print 'Error: Source file "%s" could not be read' % sys.argv[1]
        return False
    
    # Interrupts
    class InterruptJMP(Exception):
        def __init__(self, i):
            self.i = i
    class InterruptEND(Exception):
        pass
    
    # Language functions
    def f_var(arg):
        C.cursor = int(arg)
        try:
            C.var_map[arg]
        except KeyError:
            C.var_map[arg] = None
    def f_int(arg):
        C.var_map[C.cursor] = int(arg)
    def f_sum(arg):
        C.var_map[C.cursor] += C.var_map[int(arg)]
    def f_sub(arg):
        C.var_map[C.cursor] -= C.var_map[int(arg)]
    def f_gt(arg):
        C.var_map[C.cursor] = C.var_map[C.cursor] > C.var_map[int(arg)]
    def f_lt(arg):
        C.var_map[C.cursor] = C.var_map[C.cursor] < C.var_map[int(arg)]
    def f_gte(arg):
        C.var_map[C.cursor] = C.var_map[C.cursor] >= C.var_map[int(arg)]
    def f_lte(arg):
        C.var_map[C.cursor] = C.var_map[C.cursor] <= C.var_map[int(arg)]
    def f_eq(arg):
        C.var_map[C.cursor] = C.var_map[C.cursor] == C.var_map[int(arg)]
    def f_jmp(arg):
        raise InterruptJMP(int(arg))
    def f_end(arg):
        raise InterruptEND()
    def f_if(arg):
        if C.var_map[C.cursor] == 1:
            raise InterruptJMP(int(arg))
    def f_ask(arg):
        if arg[0] == '"' and arg[-1] == '"':
            arg = arg[1:-1]
        C.var_map[C.cursor] = int(raw_input(arg))
    def f_prt(arg):
        if arg[0] == '"' and arg[-1] == '"':
            arg = arg[1:-1]
        if C.cursor:
            print str(arg).replace('$', str(C.var_map[C.cursor]))
        else:
            print str(arg)
    
    # Phase two: lex file
    c = 0
    for i in range(len(src)):
        if src[i][0] == '#':
            continue
        mnemo = src[i][0:3].strip()
        arg = src[i][3:].strip()
        if mnemo == 'VAR':
            C.cmds.append((f_var, arg))
        elif mnemo == 'INT':
            C.cmds.append((f_int, arg))
        elif mnemo == 'SUM':
            C.cmds.append((f_sum, arg))
        elif mnemo == 'SUB':
            C.cmds.append((f_sub, arg))
        elif mnemo == 'ASK':
            C.cmds.append((f_ask, arg))
        elif mnemo == 'PRT':
            C.cmds.append((f_prt, arg))
        elif mnemo == 'STP':
            C.jmp_map[int(arg)] = c
            continue
        elif mnemo == 'JMP':
            C.cmds.append((f_jmp, arg))
        elif mnemo == 'END':
            C.cmds.append((f_end, None))
        elif mnemo == 'IF':
            C.cmds.append((f_if, arg))
        elif mnemo == 'GT':
            C.cmds.append((f_gt, arg))
        elif mnemo == 'LT':
            C.cmds.append((f_lt, arg))
        elif mnemo == 'GTE':
            C.cmds.append((f_gte, arg))
        elif mnemo == 'LTE':
            C.cmds.append((f_lte, arg))
        elif mnemo == 'EQ':
            C.cmds.append((f_eq, arg))
        elif not mnemo:
            print 'Empty in file %s on line %s' % (src_file, i + 1)
            return False
        else:
            print 'Unknown mnemonic "%s" detected in file "%s" on line %s' % (mnemo, src_file, i + 1)
            return False
        c += 1
    
    # Phase three: interpret code
    i = 0
    max = len(C.cmds)
    while i < max:
        try:
            cmd = C.cmds[i]
            cmd[0](cmd[1])
            i += 1
        except InterruptJMP as e:
            i = C.jmp_map[e.i]
        except InterruptEND:
            break
    
    # Return success code
    return True

# App loop
print '\nWelcome to pyYAPVM!'
print '===================\n'
main()