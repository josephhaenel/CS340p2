def RBInsert(T, z):
    y = T.nil
    x = T.root
    while x != T.nil:
        y = x
        if z.key < x.key:
            x = x.left
        else:
            x = x.right
    z.p = y
    if y == T.nil:
        T.root = z
    elif z.key < y.key:
        y.left = z
    else:
        y.right = z
    z.left = T.nil
    z.right = T.nil
    z.color = 'RED'
    RBInsertFixup(T, z)

def RBInsertFixup(T, z):
    while z.p.color == 'RED':
        if z.p == z.p.p.left:
            y = z.p.p.right
            if y.color == 'RED':
                z.p.color = 'BLACK'
                y.color = 'BLACK'
                z.p.p.color = 'RED'
                z = z.p.p
            elif z == z.p.right:
                z = z.p
                LeftRotate(T, z)
            z.p.color = 'BLACK'
            z.p.p.color = 'RED'
            RightRotate(T, z.p.p)
        else:
            y = z.p.p.left
            if y.color == 'RED':
                z.p.color = 'BLACK'
                y.color = 'BLACK'
                z.p.p.color = 'RED'
                z = z.p.p
            elif z == z.p.left:
                z = z.p
                RightRotate(T, z)
            z.p.color = 'BLACK'
            z.p.p.color = 'RED'
            LeftRotate(T, z.p.p)
    T.root.color = 'BlACK'

def LeftRotate(T, x):
    y = x.right
    x.right = y.left
    if y.left != T.nil:
        y.left.p = x
    y.p = x.p
    if x.p == T.nil:
        T.root = y
    elif x == x.p.left:
        x.p.left = y
    else:
        x.p.right = y
    y.left = x
    x.p = y


def RightRotate(T, x):
    y = x.left
    x.left = y.right
    if y.right != T.nil:
        y.right.p = x
    y.p = x.p
    if x.p == T.nil:
        T.root = y
    elif x == x.p.right:
        x.p.right = y
    else:
        x.p.left = y
    y.right = x
    x.p = y
