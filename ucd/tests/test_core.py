import ucd
t.insert(u1)
u2 = ucd.UCD('pos.eq.ra')
t.insert(u2)
print('Tree', t)
r = t.search(u1)
print('Search:', u1)
for u in r:
  print(u)


def test_tree_empty():
    t = ucd.UCDTree()

    assert len(t) == 0
    assert len(t.all()) == 0


def test_insert():
    u = ucd.UCD('meta.id;meta.main')

    t = ucd.UCDTree()
    t.insert(u)

    assert len(t) == 2
    assert len(t.all()) == 1
    

def test_search():
    u = ucd.UCD('meta.id;meta.main')

    t = ucd.UCDTree()
    t.insert(u)

    assert len(t.search('meta')) == 2
    assert len(t.search('meta.id')) == 1
    assert len(t.search('meta.main')) == 1
    r = t.search('meta')
    assert r[0].data == r[1].data
