import networkx as nx
import matplotlib.pyplot as plt

def er_diagram(table,relationships):
    graph=nx.DiGraph()

    for name in table.keys():
        graph.add_node(name)

    for relation in relationships:
        graph.add_edge(relation["from_table"],relation["to_table"],label=(f"{relation['from_column']} → "f"{relation['to_column']}"))

    fig,ax=plt.subplots(figsize=(14,10))
    pos=nx.spring_layout(graph,seed=42,k=2)

    edge_labels=nx.get_edge_attributes(graph,"label")
    
    nx.draw(graph,pos,node_size=8000,node_color="#2E86C1",edgecolors="black",linewidths=2,with_labels=True,font_size=16,arrows=True,arrowsize=20,connectionstyle='arc3,rad=0.15',ax=ax)
    nx.draw_networkx_edge_labels(graph,pos,font_size=16,edge_labels=edge_labels,ax=ax)

    ax.axis("off")

    fig.patch.set_edgecolor("grey")
    fig.patch.set_linewidth(25)
    plt.tight_layout()

    return fig