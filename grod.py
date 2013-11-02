# Get rid of doublons:


def reduce(l):
    """ gets rid, in the provided list,
        of duplicate elements
        """
    return [x[1] for x in enumerate(l) if x[1] not in l[:x[0]]]



def xreduce(l):
    """ same, but acts on iterable,
        as a generator
    """
    assert (1,2) in [(1,2), (5,6)]
    assert id((1,2)) not in [(1,2), (5,6)]

    met = set()
    for elt in l:
        if elt not in met:
            met.add(elt)
            yield(elt)

    
    
def test_reduce():
    listref = range(100)
    disturber = range(10)
    for index in listref:
        composed = listref[:index] +\
                   disturber  +\
                   listref[index:]
        expurged = reduce(composed)
        assert(expurged == listref)


def factory_tst_disturber(reducer, sizeList, sizeDist):
    ''' produces and returns the test of the reducer
        function, based on test_reduce, with the
        parameter given sizeList and sizeDist
    '''
    def factored():
        listref = range(sizeList)
        disturber = range(sizeDist)
        for index in listref:
            composed = listref[:index] +\
                       disturber  +\
                       listref[index:]
            expurged = [x for x in reducer(composed)]
            assert(expurged == listref)
    return factored

test_reduce_1 = factory_tst_disturber(reduce, 100, 10)

test_reduce_2 = factory_tst_disturber(xreduce, 1000, 10)

# previous tests not called, so I make some test that call em explicitly:
def test_1():
    test_reduce_1()

def test_2():
    test_reduce_2()



