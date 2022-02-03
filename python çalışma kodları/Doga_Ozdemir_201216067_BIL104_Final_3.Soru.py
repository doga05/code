def Yeni_Graf(__init__):
    a = Graph()
    
    #düğüm oluşturma
    c = a.insert_vertex("c düğümü")
    b = a.insert_vertex("b düğümü")
    d = a.insert_vertex("d düğümü")
    e = a.insert_vertex("e düğümü")
    h = a.insert_vertex("h düğümü")
    f = a.insert_vertex("f düğümü")
    g = a.insert_vertex("g düğümü")
    k = a.insert_vertex("k düğümü")

    #kenarlar ile düğümler arası bağ
    e1= a.insert_edge(c,b,"e1 düğümü")
    e2= a.insert_edge(b,d,"e2 düğümü")
    e3= a.insert_edge(d,e,"e3 düğümü")
    e4= a.insert_edge(h,f,"e4 düğümü")
    e5= a.insert_edge(f,g,"e5 düğümü")
    e6= a.insert_edge(h,k,"e6 düğümü")
    e7= a.insert_edge(e,h,"e7 düğümü")
    e8= a.insert_edge(d,k,"e4 düğümü")

    #düğümleri bağlayan kenarlar
    print("c-b düğümlerini", a._outgoing[c][b]._element,"bağlar")
    print("b-d düğümlerini", a._outgoing[b][d]._element,"bağlar")
    print("d-e düğümlerini", a._outgoing[d][e]._element,"bağlar")
    print("h-f düğümlerini", a._outgoing[h][f]._element,"bağlar")
    print("f-g düğümlerini", a._outgoing[f][g]._element,"bağlar")
    print("h-k düğümlerini", a._outgoing[h][k]._element,"bağlar")
    print("e-h düğümlerini", a._outgoing[e][h]._element,"bağlar")
    print("d-k düğümlerini", a._outgoing[d][k]._element,"bağlar")



