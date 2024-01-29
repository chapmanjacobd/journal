# https://github.com/renero/pyground/blob/master/pyground/utils.py

# Copyright (C) 2021 Jesus Renero <hergestridge@gmail.com>
# Licence: Apache 2.0

import random as rand
from random import randint, random
from typing import List

import numpy as np
import pandas as pd
from prettytable import PrettyTable
from scipy.special import expit  # this is the sigmoid function
from scipy.stats import lognorm, norm
from sklearn.preprocessing import RobustScaler


def print_progbar(percent: float, max: int = 20, do_print=True, **kwargs: str) -> str:
    """Prints a progress bar of max characters, with progress up to
    the passed percentage

    :param percent: the percentage of the progress bar completed
    :param max: the max width of the progress bar
    :param do_print: print the progbar or not
    :param **kwargs: optional arguments to the `print` method.

    Example

    >>> print_progbar(0.65)
    >>> "[=============·······]"

    """
    done = int(np.ceil(percent * 20))
    remain = max - done
    pb = "[" + "=" * done + "·" * remain + "]"
    if do_print is True:
        print(pb, sep="", **kwargs)
    else:
        return pb


def reset_seeds(my_seed=1):
    """
    Reset all internal seeds to same value always
    """
    np.random.seed(my_seed)
    rand.seed(my_seed)


def dict2table(dictionary: dict) -> str:
    """
    Converts a table into an ascii table.
    """
    t = PrettyTable()
    t.field_names = ["Parameter", "Value"]
    for header in t.field_names:
        t.align[header] = "l"

    def tabulate_dictionary(t: PrettyTable, d: dict, name: str = None) -> PrettyTable:
        for item in d.items():
            if isinstance(item[1], dict):
                t = tabulate_dictionary(t, item[1], item[0])
                continue
            sep = "." if name is not None else ""
            prefix = "" if name is None else name
            t.add_row([f"{prefix}{sep}{item[0]}", item[1]])
        return t

    return str(tabulate_dictionary(t, dictionary))


def random_coefficients(degree: int, prob_zero=0.2) -> List:
    """
    Generate a list of random coefficients of the degree passed

    Arguments:
        - degree: The degree of the polynomial
        - prob_zero: The probability of zeroing a coefficient.

    Returns:
        A list with coefficients for each degree.

    Examples:
        >>> polynomial = random_coefficients(3)
        >>> print(polynomial)
        >>> [ +2.22  -0.00  -3.13 ]

    """
    poly = []
    for i, d in enumerate(range(degree)):
        beta = random() * randint(-10, 10)
        zero_coeff = 0.0 if random() < prob_zero else 1.0
        poly.append(beta * zero_coeff)
    return poly


def evaluate_poly(poly: List, x: float) -> float:
    """
    Evaluates a polynomial of certain degree from the list of coefficientes

    Arguments:
        - poly: A list with the coefficients of the polynomial
        - x: the value to be pluged in onto the polynomial
    Returns:
        A float value corresponding to the evaluation of the poly on "x"

    Examples:
        >>> polynomial = random_coefficients(3)
        >>> print(polynomial)
        >>> [ -0.82  +7.96  -3.83 ]
        >>> evaluate_poly(polynomial, x=1.0)
        >>> 3.3088
    """
    v = 0.0
    for degree, beta in enumerate(poly):
        v += beta * np.power(x, degree)
    return v


def add_extra_features(num_feats: int, k: np.array, degree=3) -> np.ndarray:
    """
    Generates features dependent on the series "k", based on a random polynomial

    Arguments:
    ----------
        - num_feats: the number of features to generate
        - k: the feature on which the new ones will depend on.
        - degree: The degree of each random polynomial

    Returns:
    --------
        A matrix with k.shape[0] x num_feats new values

    Examples:
    ---------
        >>> X = np.random.rand(3, 3)
        >>> ef = add_extra_features(1, X[:, -1])
        >>> X = np.append(X, ef, axis=1)
        >>> print(X)
            [[ 0.23941487  0.1282286   0.78841238  0.34497778]
            [ 0.19726776  0.86035895  0.31766776 -0.49607576]
            [ 0.83557953  0.71509514  0.46714884 -0.28545388]]
    """
    extra_features = []
    for n in range(num_feats):
        poly = random_coefficients(degree)
        y = list(map(lambda x: evaluate_poly(poly, x), k))
        extra_features.append(y)
    return np.array(extra_features).T


def gen_toy_dataset(
    mu=0, sigma=1.0, s=0.25, sigma_z0=3.0, sigma_z1=5.0, num_samples=1000, num_feats=5, scale=False, seed=2021
):
    """
    Generate a toy dataset with 5 variables (or more), and the following causal
    relationship among them: z->x, z->t, z->y, t->y, k1, k2->k1, k3->k1

    Arguments:
    ----------
        - mu: mean for distributions of indep variables
        - sigma: variance of distributions of indep variables
        - s: mean for the lognormal distr.
        - sigma_z0: parameter to compute "x".
        - sigma_z1: parameter to compute "x".
        - num_samples: Number of samples to generate
        - num_feats: number of features to generate. Min value is 5.
        - scale: Whether scaling the resulting DataFrame with RobustScaler
                 (default is False)

    Returns:
    --------
        A dataframe with 'num_feat' features following a given causal
        relationship, and the true structure of it.


    Examples:
    ---------
        >>> from pyground.utils import gen_toy_dataset
        >>> toy_dataset, true_order = gen_toy_dataset(num_samples=5)
        >>> toy_dataset
                    z         x         t         y         k
            0 -0.165956 -1.603104  1.144675  2.854501  3.007446
            1  0.440649 -1.060788  3.766573 -0.978671  4.682616
            2 -0.999771  0.381785  2.226256  0.372360 -1.865758
            3 -0.395335 -0.256640  4.783731 -5.642051  1.923226
            4 -0.706488  0.654393  0.526440 -2.708605  3.763892
    """
    reset_seeds(my_seed=seed)

    def fx(z):
        return (sigma_z1 * sigma_z1 * z) + (sigma_z0 * sigma_z0 * (1 - z))

    def ft(z):
        return 0.75 * z + 0.25 * (1 - z)

    def fy(T):
        return expit(3.0 * (T[0] + 2.0 * (2.0 * T[1] - 1.0)))

    z = lognorm.rvs(s=0.25, scale=1.0, size=num_samples)
    x_z = [norm.rvs(loc=zi, scale=fx(zi)) for zi in z]
    t_z = np.array(list(map(ft, z)))
    y_t_z = np.array(list(map(fy, zip(z, t_z))))
    k = norm.rvs(loc=0.0, scale=1.0, size=num_samples)
    features = np.array([x_z, t_z, y_t_z, z, k]).T
    column_names = ["x", "t", "y", "z", "k"]
    true_structure = {"z": ["x", "y", "t"], "t": ["y"]}

    # Add extra features if needed
    num_extra_features = num_feats - 5
    if num_extra_features > 0:
        extra_features = add_extra_features(num_feats - 5, k)
        features = np.append(features, extra_features, axis=1)
        true_structure["k"] = []
        # set the name of the extra columns (k1, k2, k3...)
        for i in range(num_extra_features):
            column_names.append(f"k{i + 1}")
            true_structure["k"].append(f"k{i + 1}")

    # Transform everything in a dataframe
    dataset = pd.DataFrame(data=features, columns=column_names)
    dataset = dataset.astype(np.float64)
    if scale is True:
        scaler = RobustScaler()
        dataset = pd.DataFrame(data=scaler.fit_transform(dataset), columns=column_names)

    return dataset, true_structure


def matprint(mat: np.ndarray, labels: List[str]):
    """
    Pretty print an (adjcency) matrix, using same labels for columns and rows

    Arguments:
    ---------
        - mat: A squared numpy array.
        - labels: List of strings identifying columns/rows

    Returns:
    -------
        None

    Example:
        >>> a = np.array([[1, 2, 3], [5, 6, 7], [9, 10, 11]])
        >>> matprint(a, ['A','B','C'])

                   A             B             C
           -----------------------------------------
        A       +1.0000       +2.0000       +3.0000
        B       +5.0000       +6.0000       +7.0000
        C       +9.0000      +10.0000      +11.0000

    """
    max_label = max([len(lab) for lab in labels])
    print("  ")
    for i, lab in enumerate(labels):
        print("{:>12s}".format(lab), end="  ")
    bar_length = ((len(labels) - 1) * 14) + 12 + 1
    print("\n  ", "-" * bar_length)
    for j, x in enumerate(mat):
        print(("{:>" + str(max_label) + "s}").format(labels[j]), end="  ")
        for i, y in enumerate(x):
            print("{:>+12.4f}".format(y), end="  ")
        print("")


def split_data(data: np.ndarray, train_percentage: float = 0.8):
    """
    Split a numpy ndarray dataset taking a given percentage for training, and
    the remaining part for testing. The split is done by shuffling data and then
    splitting it.
    Args:
        data: np.array with data
        train_percentage: (default 0.8) the percentage to take for training.

    Returns:
        (np.array, np.array) with the two splits
    """
    assert isinstance(data, np.ndarray), "Data must be Numpy array"
    split = int(data.shape[0] * train_percentage)
    indices = np.random.permutation(data.shape[0])
    training_idx, test_idx = indices[:split], indices[split:]
    training, test = data[training_idx, :], data[test_idx, :]

    return training, test


"""
This module incorporates util functions for graphs.
"""
from pathlib import Path
from typing import Callable, Dict, List, Set, Tuple, Union

import networkx as nx
import numpy
import numpy as np
import pandas as pd
import pydot as pydot
import pydotplus
from deprecated import deprecated
from pyground.file_utils import file_exists

AnyGraph = Union[nx.Graph, nx.DiGraph]


@deprecated(version="0.234", reason="Use `compare_graphs` instead.")
def compute_graph_metrics(truth, result):
    """
    Compute graph precision and recall. Recall refers to the list of edges
    that have been correctly identified in result, and precision, to the
    ratio of edges that correctly math to those in the ground truth.

    Arguments:
        truth: A list of edges representing the true structure of the graph
               to compare with.
        result: The dag for which to measure the metrics.

    Returns:
        precision, recall values as floats

    Example:
        >>> dag1 = [('a', 'b'), ('a', 'c'), ('c', 'd'), ('c', 'b')]
        >>> dag2 = [('a', 'b'), ('a', 'c'), ('b', 'd')]
        >>> prec, rec = compute_graph_metrics(dag1, dag2)
        >>> print(prec, rec)
        >>> 0.75 0.5

    """
    # Convert the ground truth and target into a set of tuples with edges
    if not isinstance(truth, set):
        ground_truth = set([tuple(pair) for pair in truth])
    elif isinstance(truth, set):
        ground_truth = truth
    else:
        raise TypeError("Truth argument must be a list or a set.")
    if not isinstance(result, set):
        target = set([tuple(pair) for pair in result])
    elif isinstance(result, set):
        target = result
    else:
        raise TypeError("Results argument must be a list or a set.")

    # Set the total number of edges if ground truth skeleton
    total = max([float(len(ground_truth)), float(len(target))])
    true_positives = len(ground_truth.intersection(target))
    false_positives = len(target - ground_truth.intersection(target))
    precision = 1.0 - (false_positives / total)
    recall = true_positives / total

    return precision, recall


def build_graph(list_nodes: List, matrix: np.ndarray, threshold=0.05, zero_diag=True) -> nx.Graph:
    """
    Builds a graph from an adjacency matrix. For each position i, j, if the
    value is greater than the threshold, an edge is added to the graph. The
    names of the vertices are in the list of nodes pased as argument, whose
    order must match the columns in the matrix.

    The diagonal of the matrix is set to zero to avoid inner edges, but this
    behavior can be overridden by setting zero_diag to False.

    Args:
        list_nodes: a list with the names of the graph's nodes.
        matrix: a numpy ndarray with the weights to be used
        threshold: the threshold above which a vertex is created in the graph
        zero_diag: boolean indicating whether zeroing the diagonal. Def True.

    Returns:
        nx.Graph: A graph with edges between values > threshold.

    Example:
        >>> matrix = np.array([[0., 0.3, 0.2],[0.3, 0., 0.2], [0.0, 0.2, 0.]])
        >>> dag = build_graph(['a','b','c'], matrix, threshold=0.1)
        >>> dag.edges()
            EdgeView([('a', 'b'), ('a', 'c'), ('b', 'c')])
    """
    M = np.copy(matrix)
    if M.shape[0] != M.shape[1]:
        raise ValueError("Matrix must be square")
    if M.shape[1] != len(list_nodes):
        raise ValueError("List of nodes doesn't match number of rows/cols")
    if zero_diag:
        np.fill_diagonal(M, 0.0)
    graph = nx.Graph()
    for (i, j), x in np.ndenumerate(M):
        if M[i, j] > threshold:
            graph.add_edge(list_nodes[i], list_nodes[j], weight=M[i, j])
    for node in list_nodes:
        if node not in graph.nodes():
            graph.add_node(node)
    return graph


def graph_print_edges(graph: nx.Graph):
    """
    Pretty print the nodes of a graph, with weights

    Args:
         graph: the graph to be printed out.
    Returns:
        None.
    Example:
        >>> matrix = np.array([[0., 0.3, 0.2],[0.3, 0., 0.2], [0.0, 0.2, 0.]])
        >>> dag = build_graph(['a','b','c'], matrix, threshold=0.1)
        >>> graph_print_edges(dag)
            Graph contains 3 edges.
            a –– b +0.3000
            a –– c +0.2000
            b –– c +0.2000

    """
    mx = max([len(s) for s in list(graph.nodes)])
    edges = list(graph.edges)
    print(f"Graph contains {len(edges)} edges.")

    # Check if this graph contain weight information
    get_edges = getattr(graph, "edges", None)
    if callable(get_edges):
        edges_weights = get_edges(data="weight")
    else:
        edges_weights = edges

    # Printout
    for edge in edges_weights:
        if len(edge) == 3 and edge[2] is not None:
            print(("{:" + str(mx) + "s} –– {:" + str(mx) + "s} {:+.4f}").format(edge[0], edge[1], edge[2]))
        else:
            print(("{:" + str(mx) + "s} –– {:" + str(mx) + "s}").format(edge[0], edge[1]))


@deprecated(version="0.2.34", reason="Use graph_print_edges()")
def print_graph_edges(graph: nx.Graph):
    graph_print_edges(graph)


def graph_to_adjacency(graph: AnyGraph, weight_label: str = "weight") -> numpy.ndarray:
    """
    A method to generate the adjacency matrix of the graph. Labels are
    sorted for better readability.

    Args:
        graph: (Union[Graph, DiGraph]) the graph to be converted.
        weight_label: the label used to identify the weights.

    Return:
        graph: (numpy.ndarray) A 2d array containing the adjacency matrix of
            the graph.
    """
    symbol_map = {"o": 1, ">": 2, "-": 3}
    labels = sorted(list(graph.nodes))  # [node for node in self]
    mat = np.zeros((len(labels), (len(labels))))
    for x in labels:
        for y in labels:
            if graph.has_edge(x, y):
                if bool(graph.get_edge_data(x, y)):
                    if y in graph.get_edge_data(x, y).keys():
                        mat[labels.index(x)][labels.index(y)] = symbol_map[graph.get_edge_data(x, y)[y]]
                    else:
                        mat[labels.index(x)][labels.index(y)] = graph.get_edge_data(x, y)[weight_label]
                else:
                    mat[labels.index(x)][labels.index(y)] = 1
    return mat


def graph_from_adjacency(
    adjacency: np.ndarray, node_labels=None, th=None, inverse: bool = False, absolute_values: bool = False
) -> nx.DiGraph:
    """
    Manually parse the adj matrix to shape a dot graph

    Args:
        adjacency: a numpy adjacency matrix
        node_labels: an array of same length as nr of columns in the adjacency
            matrix containing the labels to use with every node.
        th: (float) weight threshold to be considered a valid edge.
        inverse (bool): Set to true if rows in adjacency reflects where edges are
            comming from, instead of where are they going to.
        absolute_values: Take absolute value of weight label to check if its greater
            than the threshold.

    Returns:
         The Graph (DiGraph)
    """
    G = nx.DiGraph()
    G.add_nodes_from(range(adjacency.shape[1]))

    # What to do with absolute values?
    not_abs = lambda x: x
    w_val = np.abs if absolute_values else not_abs
    weight_gt = lambda w, thresh: w != 0.0 if thresh is None else w_val(w) > thresh

    # A method to check if weight is greater than threshold, only if has been specified
    # def check_weight(w_val, threshold):
    #     if threshold is None:
    #         return True
    #     return weight(w_val) > threshold

    # Do I have a threshold to consider?
    for i, row in enumerate(adjacency):
        for j, value in enumerate(row):
            if inverse:
                if weight_gt(adjacency[j][i], th):
                    G.add_edge(i, j, weight=w_val(adjacency[j][i]))
            else:
                if weight_gt(value, th):
                    G.add_edge(i, j, weight=w_val(value))  # , arrowhead="normal")
    # Map the current column numbers to the letters used in toy dataset
    if node_labels is not None and len(node_labels) == adjacency.shape[1]:
        mapping = dict(zip(sorted(G), node_labels))
        G = nx.relabel_nodes(G, mapping)

    return G


def graph_from_adjacency_file(file: Union[Path, str], th=0.0) -> Tuple[nx.DiGraph, pd.DataFrame]:
    """
    Read Adjacency matrix from a file and return a Graph

    Args:
        file: (str) the full path of the file to read
        th: (float) weight threshold to be considered a valid edge.
    Returns:
        DiGraph, DataFrame
    """
    df = pd.read_csv(file, dtype="str")
    df = df.astype("float64")
    labels = list(df)
    G = graph_from_adjacency(df.values, node_labels=labels, th=th)
    return G, df


def graph_to_adjacency_file(graph: AnyGraph, output_file: Union[Path, str]):
    """
    A method to write the adjacency matrix of the graph to a file. If graph has
    weights, these are the values stored in the adjacency matrix.

    Args:
        graph: (Union[Graph, DiGraph] the graph to be saved
        output_file: (str) The full path where graph is to be saved
    """
    mat = graph_to_adjacency(graph)
    labels = sorted(list(graph.nodes))
    f = open(output_file, "w")
    f.write(",".join([f"{label}" for label in labels]))
    f.write("\n")
    for i in range(len(labels)):
        f.write(f"{labels[i]}")
        f.write(",")
        f.write(",".join([str(point) for point in mat[i]]))
        f.write("\n")
    f.close()


def graph_from_dot_file(dot_file: Union[str, Path]) -> nx.DiGraph:
    """Returns a NetworkX DiGraph from a DOT FILE."""
    dot_object = pydot.graph_from_dot_file(dot_file)
    dotplus = pydotplus.graph_from_dot_data(dot_object[0].to_string())
    dotplus.set_strict(True)
    return nx.nx_pydot.from_pydot(dotplus)


def graph_from_dot(dot_object: pydot.Dot) -> nx.DiGraph:
    """Returns a NetworkX DiGraph from a DOT object."""
    dotplus = pydotplus.graph_from_dot_data(dot_object.to_string())
    dotplus.set_strict(True)
    return nx.nx_pydot.from_pydot(dotplus)


def graph_to_dot(g: AnyGraph) -> pydot.Dot:
    """Converts a graph into a dot structure"""
    return nx.drawing.nx_pydot.to_pydot(g)


def graph_to_dot_file(g: AnyGraph, location: Union[Path, str]) -> None:
    """Converts graph into a pyDot object and saves it to specified location"""
    nx.drawing.nx_pydot.write_dot(g, location)


def graph_fom_csv(
    graph_file: Union[Path, str],
    graph_type: Callable,
    source_label="from",
    target_label="to",
    edge_attr_label=None,
):
    """
    Read Graph from a CSV file with "FROM", "TO" and "WEIGHT" fields

    Args:
        graph_file: a full path with the filename
        graph_type: Graph or DiGraph
        source_label: name of the "from"/cause column in the dataset
        target_label: name of the "to"/effect column in the dataset
        edge_attr_label: name of the weight, if any (def: None)

    Returns:
        networkx.Graph or networkx.DiGraph
    """
    edges = pd.read_csv(graph_file)
    Graphtype = graph_type()
    ugraph = nx.from_pandas_edgelist(
        edges,
        source=source_label,
        target=target_label,
        edge_attr=edge_attr_label,
        create_using=Graphtype,
    )
    return ugraph


def graph_to_csv(graph: AnyGraph, output_file: Union[Path, str]):
    """
    Save a GrAPH to CSV file with "FROM", "TO" and "CSV"
    """
    if file_exists(output_file, "."):
        output_file = f"New_{output_file}"
    skeleton = pd.DataFrame(list(graph.edges(data="weight")))
    skeleton.columns = ["from", "to", "weight"]
    skeleton.to_csv(output_file, index=False)


def graph_weights(graph: AnyGraph, field="weight"):
    """
    Returns graph weights, or the name of the data field for each edge in the graph.

    Args:
        graph (Graph or DiGraph): the graph from wich to extract the field values
        field (str): The name of the field for which to extract the values. By
            default it is 'weight'.

    Returns:
        Numpy.array with the values of the specified field.
    """
    return np.array([data[field] if field in graph[s][t] else 0.0 for s, t, data in graph.edges(data=True)])


def graph_filter(graph: Union[Path, str], threshold, field="weight", lower: bool = False):
    """
    Filter a graph taking only those edges whose weight is > threshold

    Args:
        graph: The graph to be filtered
        threshold: The minimum value to act as filter for edges weight
        field (str): The name of the weight to use as filter. Default is weight.
        lower (bool): If True the method returns edges whose weight is < threshold.

    Returns:
        A graph (same type as original) with only the edges filtered.
    """
    GType = type(graph)
    ng = GType()
    ng.add_nodes_from(graph)
    for u, v, d in graph.edges(data=True):
        comparison = d[field] < threshold if lower else d[field] >= threshold
        if comparison:
            ng.add_edge(u, v, weight=d[field])
    return ng


def graph_from_parent_ids(parents_list: Dict[int, List[int]], node_names: List[str]) -> nx.DiGraph:
    """
    Build a graph from a list of parent ids. Each key in the dict is the id number
    of a node whose parents are in the values for that key.

    Example: {3: [], 0: [3], 2: [3, 0], 4: [3, 0, 2], 1: [3, 0, 2, 4]}

    The node "3" has no parents, the parent of "0" is "3", and so on.

    Arguments:
         parents_list (Dict[int, List[int]]): a dictionary with nodes as keys and
            lists of parents for each node as list of values.
        node_names (List[str]): The names of the nodes.

    Returns:
        A directed graph representing the hierarchy represented by the list of parents
    """
    g = nx.DiGraph()
    g.add_nodes_from(node_names)
    for child in parents_list.keys():
        parents = parents_list[child]
        if not parents:
            continue
        for parent in parents:
            g.add_edge(node_names[parent], node_names[child])

    return g


def graph_from_dictionary(d: Dict[str, Union[str, List[str]]]) -> AnyGraph:
    g = nx.DiGraph()
    for node, parents in d.items():
        for parent in parents:
            g.add_edge(parent, node)
    return g


def graph_union(graphs: List[AnyGraph], nodes: List[Union[str, int]]):
    """
    Computes the intersection of several graphs as the graph with the edges
    in common among all them. The resulting edges' weights are the nr of times
    that they are present in the set.

    Args:
        graphs: (List[nx.Graph] or List[nx.DiGraph]) A list of graphs
        nodes: Default list of nodes for the resulting graph, to ensure that
            graph is populated with at least these nodes, even though not all
            edges link them entirely

    Returns:
        nx.Digraph with the edges in common, weighted by the nr of times they appear
    """
    assert len(graphs) > 1, "This method needs more than one graph to compute intersection"
    G = nx.DiGraph()
    if nodes is not None:
        G.add_nodes_from(nodes)
    for g in graphs:
        for u, v, d in g.edges(data=True):
            if G.has_edge(u, v):
                G[u][v]["weight"] += 1
                continue
            G.add_edge(u, v, weight=1)

    return G


def graph_biconnections(g) -> Set[Tuple[str, str]]:
    """
    Returns all bidirectional connections in a graph.
    Args:
        g: a networkx graph

    Returns:
        A set with the pairs of nodes bidirectionally connected.
    """

    def have_bidirectional_relationship(G, node1, node2):
        return G.has_edge(node1, node2) and G.has_edge(node2, node1)

    biconnections = set()
    for u, v in g.edges():
        if u > v:  # Avoid duplicates, such as (1, 2) and (2, 1)
            v, u = u, v
        if have_bidirectional_relationship(g, u, v):
            biconnections.add((u, v))

    return biconnections


import random
import string
from typing import List

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import pydot
import pydotplus
from IPython.display import Image, display
from pydot import Dot
from pyground.graph_utils import AnyGraph, graph_to_adjacency


def plot_dot(dot_object: pydot.Dot, **kwargs) -> None:
    """Displays a DOT object in the notebook"""
    image = Image(dot_object.create_png(), **kwargs)
    display(image)


def dot_graph(
    G: nx.DiGraph,
    undirected=False,
    plot: bool = True,
    name: str = "my_dotgraph",
    odots: bool = True,
    **kwargs,
) -> Dot:
    """
    Display a DOT of the graph in the notebook.

    Args:
        G (nx.Graph or DiGraph): the graph to be represented.
        undirected (bool): default False, indicates whether the plot is forced
            to contain no arrows.
        plot (bool): default is True, this flag can be used to simply generate
            the object but not plot, in case the object is needed to generate
            a PNG version of the DOT, for instance.
        name (str): the name to be embedded in the Dot object for this graph.
        odots (bool): represent edges with biconnections with circles (odots). if
            this is set to false, then the edge simply has no arrowheads.

    Returns:
        pydot.Dot object
    """
    if len(list(G.edges())) == 0:
        return None
    # Obtain the DOT version of the NX.DiGraph and visualize it.
    if undirected:
        G = G.to_undirected()
        dot_object = nx.nx_pydot.to_pydot(G)
    else:
        # Make a dot Object with edges reflecting biconnections as non-connected edges
        # or arrowheads as circles.
        dot_str = "strict digraph" + name + "{\nconcentrate=true;\n"
        for node in G.nodes():
            dot_str += f"{node};\n"
        if odots:
            options = "[arrowhead=odot, arrowtail=odot, dir=both]"
        else:
            options = "[dir=none]"
        for u, v in G.edges():
            if G.has_edge(v, u):
                dot_str += f"{u} -> {v} {options};\n"
            else:
                dot_str += f"{u} -> {v};\n"
        dot_str += "}\n"
        # src = graphviz.Source(dot_str)
        dot_object = pydotplus.graph_from_dot_data(dot_str)
        # old way of getting the dot_object
        # > dot_object = nx.nx_pydot.to_pydot(G)

    # This is to display single arrows with two heads instead of two arrows with
    # one head towards each direction.
    dot_object.set_concentrate(True)
    if plot:
        plot_dot(dot_object, **kwargs)

    return dot_object


def dot_graphs(
    dags: List[AnyGraph],
    dag_names: List[str] = None,
    num_rows=1,
    num_cols=2,
    undirected: bool = False,
    odots: bool = True,
    fig_size=(12, 8),
    **kwargs,
):
    """
    Make a plot with several Dots of the dags passed.
    Args:
        dags: A list of netowrkx graph objects
        dag_names: A list of names for the graphs passed
        num_rows: number of rows to use when creating subplots
        num_cols: number of cols to use when creating subplots
        undirected: whether the dot representation must be undirected (no arrows)
        odots: whether represent biconnections with circles in both directions.
        fig_size: tuple with the fig size for the plot.
        **kwargs: optional arguments to be passed to matplotlib

    Returns:
        None
    """
    pngs = []
    label = "".join(random.choice(string.ascii_lowercase) for _ in range(6))
    for d, dag in enumerate(dags):
        d_obj = dot_graph(dag, undirected=undirected, odots=odots, plot=False, **kwargs)
        output = f"./png/dag_{label}_{d}.png"
        d_obj.write_png(output)
        pngs.append(output)

    # Represent all the DAGs together
    fig = plt.figure(figsize=fig_size)
    # f, ax = plt.subplots(num_rows, num_cols, figsize=fig_size)
    images = [plt.imread(png) for png in pngs]
    if dag_names is None:
        dag_names = [f"dag_{i}" for i in range(len(dags))]

    if len(dags) > num_cols and num_rows == 1:
        num_cols = len(dags)
    for i in range(num_rows * num_cols):
        # row = int(i / num_cols)
        # col = np.round(((i / num_cols) - row) * num_cols).astype(int)
        ax = fig.add_subplot(num_rows, num_cols, i + 1)
        if i >= len(pngs):  # empty image https://stackoverflow.com/a/30073252
            npArray = np.array([[[255, 255, 255, 255]]], dtype="uint8")
            ax.imshow(npArray, interpolation="nearest")
            ax.set_axis_off()
        else:
            ax.imshow(images[i])
            ax.set_title(f"{dag_names[i].upper()}")
            ax.set_axis_off()

    title = "Causal DAGs"
    fig.suptitle(title, fontsize=16)
    plt.tight_layout()
    plt.show()


def plot_graph(graph: nx.DiGraph) -> None:
    """Plot a graph using default Matplotlib methods"""
    pos = nx.circular_layout(graph, scale=20)
    nx.draw(
        graph, pos, nodelist=graph.nodes(), node_color="lightblue", node_size=800, width=2, alpha=0.9, with_labels=True
    )
    plt.show()


def plot_graphs(G: nx.MultiDiGraph, H: nx.DiGraph) -> None:
    """Plot two graphs side by side."""
    pos1 = nx.circular_layout(G, scale=20)
    pos2 = nx.circular_layout(H, scale=20)
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
    ax = axes.flatten()
    nx.draw_networkx(G, pos1, node_color="lightblue", node_size=800, edge_color="orange", width=2, alpha=0.9, ax=ax[0])
    ax[0].set_axis_off()
    ax[0].set_title("Ground Truth")
    nx.draw_networkx(
        H, pos2, node_color="lightblue", node_size=800, edge_color="lightblue", width=2, alpha=0.9, ax=ax[1]
    )
    ax[1].set_axis_off()
    ax[1].set_title("Other")
    plt.tight_layout()
    plt.show()


def plot_compared_graph(G: nx.DiGraph, H: nx.DiGraph) -> None:
    """
    Iterate over the composed graph's edges and nodes, and assign to these a
    color depending on which graph they belong to (including both at the same
    time too). This could also be extended to adding some attribute indicating
    to which graph it belongs too.
    Intersecting nodes and edges will have a magenta color. Otherwise they'll
    be green or blue if they belong to the G or H Graph respectively
    """
    GH = nx.compose(G, H)
    # set edge colors
    edge_colors = dict()
    for edge in GH.edges():
        if G.has_edge(*edge):
            if H.has_edge(*edge):
                edge_colors[edge] = "black"
                continue
            edge_colors[edge] = "lightgreen"
        elif H.has_edge(*edge):
            edge_colors[edge] = "orange"

    # set node colors
    G_nodes = set(G.nodes())
    H_nodes = set(H.nodes())
    node_colors = []
    for node in GH.nodes():
        if node in G_nodes:
            if node in H_nodes:
                node_colors.append("lightgrey")
                continue
            node_colors.append("lightgreen")
        if node in H_nodes:
            node_colors.append("orange")

    pos = nx.circular_layout(GH, scale=20)
    nx.draw(
        GH,
        pos,
        nodelist=GH.nodes(),
        node_color=node_colors,
        edgelist=edge_colors.keys(),
        edge_color=edge_colors.values(),
        node_size=800,
        width=2,
        alpha=0.5,
        with_labels=True,
    )


def plot_adjacency(g: nx.Graph, ax=None):
    """
    Plots the adjacency matrix as explained by scikit contributor
    Andreas Mueller in Columbia lectures, ordering and grouping
    (numerical) features with higher correlation.

    Returns:
        None
    """
    mat = graph_to_adjacency(g)
    features = sorted(list(g.nodes))
    num_features = len(features)

    if ax is None:
        _, ax = plt.subplots()
    plt.xticks(fontsize=10)
    ax.set_title("Grouped Adjacency Matrix")
    ax.matshow(mat, interpolation="nearest")
    for (j, i), label in np.ndenumerate(mat):
        ax.text(i, j, f"{label:.2g}", ha="center", va="center")
    ax.xaxis.set_ticks_position("bottom")
    ax.set_xticks(range(num_features))
    ax.set_xticklabels(features)
    ax.set_yticks(range(num_features))
    ax.set_yticklabels(features)


import errno
import glob
import os
import pickle
from os.path import dirname, join, realpath
from pathlib import Path

import joblib
import pandas as pd
from pandas import DataFrame
from sklearn.preprocessing import MinMaxScaler


def file_exists(given_filepath: str, my_dir: str) -> bool:
    """
    Check if the file exists as specified in argument, or try to find
    it using the local path of the script

    :param given_filepath:
    :return: Whether the file has been found.
    """
    if os.path.exists(given_filepath) is True:
        return True
    else:
        new_filepath = os.path.join(my_dir, given_filepath)
        if os.path.exists(new_filepath) is True:
            return True
        else:
            return False


def locate_file(given_filepath: str, my_dir: str) -> str:
    """
    Check if the file exists as specified in argument, or try to find
    it using the local path of the script
    :param given_filepath:
    :return: The path where the file is or None if it couldn't be found
    """
    if os.path.exists(given_filepath) is True:
        filepath = given_filepath
    else:
        new_filepath = os.path.join(my_dir, given_filepath)
        if os.path.exists(new_filepath) is True:
            filepath = new_filepath
        else:
            raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), new_filepath)
    print(f"filepath = {filepath}")
    return filepath


def valid_output_name(filename: str, path: str, extension=None) -> str:
    """
    Builds a valid name. In case there's another file which already exists
    adds a number (1, 2, ...) until finds a valid filename which does not
    exist.

    Returns
    -------
    The filename if the name is valid and file does not exists,
            None otherwise.

    Params
    ------
    filename: str
        The base filename to be set.
    path: str
        The path where trying to set the filename
    extension:str
        The extension of the file, without the dot '.' If no extension is
        specified, any extension is searched to avoid returning a filepath
        of an existing file, no matter what extension it has.
    """
    # path = file_exists(path, dirname(realpath(__file__)))
    if extension:
        base_filepath = join(path, filename) + ".{}".format(extension)
    else:
        base_filepath = join(path, filename)
    output_filepath = base_filepath
    idx = 1
    while len(glob.glob(f"{output_filepath}*")) > 0:
        if extension:
            output_filepath = join(path, filename) + "_{:d}.{}".format(idx, extension)
        else:
            output_filepath = join(path, filename + "_{}".format(idx))
        idx += 1

    # print(f'output_filepath: {output_filepath}')
    return output_filepath


def change_extension_to(original_file: str, new_extension: str) -> str:
    """
    Given a filename, returns a new filename with the same basename but with a
    different extension, specified in argument.

    Args:
          original_file: (str) the filename change extension
          new_extension: (str) the new extension to be used with the filename
                               Do not use dots in the new extension.

    Returns:
          str: the filename with the original extension replaced with the new
    """
    if "." in new_extension and new_extension.indes(".") == 0:
        new_extension = new_extension[1:]
    try:
        pos = original_file.index(".")
    except ValueError:
        return original_file + "." + new_extension
    if pos == original_file.rindex("."):
        return original_file[:pos] + "." + new_extension
    else:
        pos = original_file.rindex(".")
        return original_file[:pos] + "." + new_extension


def save_dataframe(
    name: str, df: DataFrame, output_path: str, cols_to_scale: list = None, scaler_name: str = None, index: bool = True
) -> (str, str):
    """
    Save the data frame passed, with a valid output name in the output path
    scaling the columns specified, if applicable.

    :param name: the name to be used to save the df to file
    :param df: the dataframe
    :param output_path: the path where the df is to be saved
    :param cols_to_scale: array with the names of the columns to scale
    :param scaler_name: baseName of the file where saving the scaler used.
    :param index: save index in the csv

    :return: the full path of the file saved
    """
    data = df.copy()
    file_name = valid_output_name(name, output_path, "csv")
    if cols_to_scale is not None:
        scaler = MinMaxScaler(feature_range=(-1.0, 1.0))
        data[cols_to_scale] = scaler.fit_transform(data[cols_to_scale])
        # Save the scaler used
        scaler_name = valid_output_name(scaler_name, output_path, "pickle")
        joblib.dump(scaler, scaler_name)
    data.round(4).to_csv(file_name, index=index)

    return file_name, scaler_name


def scale(x, minimum, peak_to_peak):
    return (x - minimum) / peak_to_peak


def unscale(y, minimum, peak_to_peak):
    return (peak_to_peak * y) + minimum


def scale_columns(df, mx):
    """
    Scale columns from a dataframe to 0..1 range.

    :param df:              the dataframe
    :param mn:              the minimum value of the series
    :param mx:              the maximum value of the series

    :return: The data frame scaled
    """
    df = df.apply(lambda x: scale(x, minimum=0.0, peak_to_peak=mx - 0.0))
    return df


def unscale_columns(df, mx):
    """
    UN_Scale columns from a dataframe to 0..1 range.

    :param df:              the dataframe
    :param mn:              the minimum value of the series
    :param mx:              the maximum value of the series

    :return: The data frame scaled
    """
    df = df.apply(lambda y: unscale(y, minimum=0.0, peak_to_peak=mx - 0.0))
    return df


def unscale_results(results, maximum):
    df = results.copy()
    # Un-scale results money info with manually set ranges for data
    # in params file.
    to_unscale = ["price", "forecast", "budget", "cost", "value", "profit", "balance"]
    df[to_unscale] = unscale_columns(df[to_unscale], maximum)

    return df


def read_ohlc(filename: str, csv_dict: dict, **kwargs) -> DataFrame:
    """
    Reads a filename passed as CSV, renaming columns according to the
    dictionary passed.
    :param filename: the file with the ohlcv columns
    :param csv_dict: the dict with the names of the columns
    :return: the dataframe
    """
    filepath = file_exists(filename, dirname(realpath(__file__)))
    df = pd.read_csv(filepath, **kwargs)

    # Reorder and rename
    columns_order = [csv_dict[colname] for colname in csv_dict]
    df = df[columns_order]
    df.columns = csv_dict.keys()

    return df


def save_experiment(obj_name: str, folder: str, results: dict):
    """
    Creates a folder for the experiment and saves results. Results is a
    dictionary that will be saved as an opaque pickle. When the experiment will
    require to be loaded, the only parameter needed are the folder name.

    Args:
        obj_name (str): the name to be given to the pickle file to be saved. If
            a file already exists with that name, a file with same name and a
            extension will be generated.
        folder (str): a full path to the folder where the experiment is to be saved.
            If the folder does not exist it will be created.
        results (obj): the object to be saved as experiment. This is typically a
            dictionary with different items representing different parts of the
            experiment.

    Return:
        (str) The name under which the experiment has been saved
    """
    if not os.path.exists(folder):
        Path(folder).mkdir(parents=False, exist_ok=True)
    output = valid_output_name(obj_name, folder, extension="pickle")
    with open(output, "wb") as handle:
        pickle.dump(results, handle, protocol=pickle.HIGHEST_PROTOCOL)

    return output


def load_experiment(obj_name: str, folder: str):
    """
    Loads a pickle from a given folder name. It is not necessary to add the "pickle"
    extension to the experiment name.

    Args:
        obj_name (str): The name of the object saved in pickle format that is to be
            loaded.
        folder (str): A full path where looking for the experiment object.

    Returns:
        An obj loaded from a pickle file.
    """
    if Path(obj_name).suffix == "" or Path(obj_name).suffix != "pickle":
        ext = ".pickle"
    else:
        ext = ""

    experiment = f"{str(Path(folder, obj_name))}{ext}"
    with open(experiment, "rb") as h:
        return pickle.load(h)


import warnings

import numpy as np
import scipy.stats as stats
import seaborn as sns
from matplotlib import gridspec
from matplotlib import pyplot as plt


def plot_distribution(values: np.ndarray, perc=None, perc_pos=0, th=None, **kwargs):
    """
    Plots histogram, density and values sorted. If percentile parameter is set,
    it is also plotted the position from which the values account for that
    percentage of the total sum.

    Parameters:
        - values (np.array): list of values (1D).
        - perc (float): The percentage of the total sum of the values, or the
            position in the CDF from which to consider the values to extract.
        - th (float): The value in the distribution used as lower limit to
            compute the percentage of samples above it.
        - verbose(bool): Verbosity

    Return:
        - (threshold, position) (float, int): the value from which the cum
            sum accounts for the 'percentile' percentage of the total sum, and
            the position in the sorted list of values where that threshold is
            located.
    """
    compact = kwargs.get("compact", False)
    fsize = (11, 2) if compact else (8, 6)

    fig = plt.figure(tight_layout=True, figsize=fsize)
    gs = gridspec.GridSpec(1, 4) if compact else gridspec.GridSpec(2, 2)

    ax1 = fig.add_subplot(gs[0, 0])
    ax1.hist(values, edgecolor="white", alpha=0.5, bins=25)
    ax1.set_title(f"Histogram (threshold={th:.2g})", fontsize=9)

    ax2 = fig.add_subplot(gs[0, 1])
    sns.kdeplot(values, ax=ax2, bw_adjust=0.5)
    ax2.set_title(f"Density (threshold={th:.2g})", fontsize=9)
    ax2.set(ylabel=None)

    if th > 0.0:
        ax1.axvline(th, linewidth=0.5, c="red", linestyle="dashed")
        ax2.axvline(th, linewidth=0.5, c="red", linestyle="dashed")

    ax3 = fig.add_subplot(gs[0, 2]) if compact else fig.add_subplot(gs[1, 0])
    x, y = np.arange(len(values)), np.sort(values)
    ax3.plot(x, y)
    if perc is not None:
        if perc < 1.0:
            ax3.set_title(f"{perc * 100:.0f}% of rev.cum.sum (>{th:.2f})", fontsize=9)
        else:
            cdf = (y[int(perc_pos) :].sum() / y.sum()) * 100.0
            ax3.set_title(f"Pos.{int(perc_pos)} (th. > {th:.2g}) = {cdf:.0f}%", fontsize=9)
        ax3.axvline(perc_pos, linewidth=0.5, c="red", linestyle="dashed")
        ax3.fill_between(x, min(y), y, where=x >= perc_pos, alpha=0.2)
    else:
        ax3.set_title("Ordered values", fontsize=9)

    ax4 = fig.add_subplot(gs[0, 3]) if compact else fig.add_subplot(gs[1, 1])
    xe = np.sort(values)
    ye = np.arange(1, len(xe) + 1) / float(len(xe))
    ax4.plot(xe, ye)
    if perc is not None:
        cdf = ye[np.max(np.where(xe < th))] * 100.0
        if perc < 1.0:
            ax4.set_title(
                f"rev.ECDF {perc * 100:.0f}% (th.> {th:.2g}) ~ {cdf:.0f}%",
                fontsize=9,
            )
        else:
            ax4.set_title(
                f"Pos.{int(perc_pos)} of rev.ECDF (th.>{th:.2g}) ~ {cdf:.0f}%",
                fontsize=9,
            )
        ax4.fill_between(xe, min(ye), ye, where=xe >= th, alpha=0.2)
        ax4.axvline(th, linewidth=0.5, c="red", linestyle="dashed")
    else:
        ax4.set_title("ECDF", fontsize=9)

    fig.align_labels()
    plt.tight_layout()
    plt.show()


def get_threshold(values, percentile=0.8, **kwargs):
    """
    Computes the value from which either: the accumulated sum of values represent
    the percentage passed as argument (<1), or the number of values in the lower range
    equals the value passed (>1). The value is computed sorting the values in
    descending order, so the this metric determines what are the most important values.

    Parameters:
        - values (np.array): List of values (1D) to analyze
        - percentile (float): The percentage of the total sum of the values.

    Returns:
        float with either the threshold in the values that account for the percentile
            passed, or the percentage of distribution above the threshold passed.

    Examples:
        >>>> a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        >>>> get_threshold(a, verbose=True)
        Values shape: 10
        Sum values: 55.00
        Sum@Percentile(0.80): 44.00
        Position @ percentile 0.80 in cum.sum: 6
        Threshold (under perc.0.80): 7.00
    """
    verbose = kwargs.get("verbose", False)
    sum_values = np.sum(values)
    cumsum = np.cumsum(sorted(values, reverse=True))
    if verbose:
        print("Computing threshold")
        print(f"Values shape: {values.shape[0]}")
        print(f"Sum values: {sum_values:.2f}")
        if percentile < 1.0:
            print(f"Sum@Percentile({percentile:.2f}): {sum_values * percentile:.2f}")
    # Substract because cumsum is reversed
    if percentile < 1.0:
        perc_sum = sum_values * percentile
        pos_q = values.shape[0] - len(np.where(cumsum < perc_sum)[0])
    else:
        pos_q = float(percentile)
    if pos_q == values.shape[0]:
        pos_q -= 1
    if verbose:
        if percentile < 1.0:
            print(f"Position @ percentile {percentile:.2f} in cum.sum: {pos_q}")
        else:
            print(f"Position in values: {int(pos_q)}")
    threshold = sorted(values)[int(pos_q)]
    if verbose:
        print(f"Threshold @ p. {percentile:.2f}): {threshold:.2f}")
    return threshold, pos_q


def get_percentile(values, threshold, **kwargs):
    """
    Computes the percentage of distribution that represents the values above a given
    threshold.

    Parameters:
        - values (np.array): List of values (1D) to analyze
        - threshold (float): The lower value to be considered in the list of values.

    Returns:
        float with either the threshold in the values that account for the percentile
            passed, or the percentage of distribution above the threshold passed.

    Examples:
        >>>> a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        >>>> get_percentile(a, 5, verbose=True)
    """
    sum_values = np.sum(values)
    verbose = kwargs.get("verbose", False)
    ord_values = np.array(sorted(values, reverse=True))
    new_values = ord_values[ord_values >= threshold]
    num_new_values = len(new_values)
    sum_new_values = np.sum(new_values)
    perc = sum_new_values / sum_values
    pos = values.shape[0] - num_new_values
    if verbose:
        print("Computing percentile")
        print(f"Sum values: {sum_values:.2f}")
        print(f"Len values above {threshold}: {num_new_values}")
        print(f"Position @ threshold: {pos}")
        print(f"Sum upper values: {sum_new_values:.2f}")
        print(f"Values above threshold: {perc:.2f}")

    return perc, pos


def get_boundaries(values, percentile=None, threshold=None, **kwargs):
    """
    Search for the threshold for a given percentile, the percentile for a given
    threshold, and plots the results if the corresponding flag is set to True.
    Args:
        values (np.array): the 1D values
        percentile (float or int): represents the percentage of the value, from
            right of the distribution to consider. If an integer, represents the
            position in the descending list of values to be used as lower boundary.
        threshold (float): A lower limit for the values in the distribution.
        **kwargs: 'plot', 'verbose'.

    Returns:
        The threshold, the percentage of distribution and the position in the
            descending list of values where those cutoffs have been found.
    """
    if percentile is not None:
        th, pos = get_threshold(values, percentile=percentile, **kwargs)
        perc = percentile
    elif threshold is not None:
        perc, pos = get_percentile(values, threshold=threshold, **kwargs)
        th = threshold
    else:
        perc = None
        th = np.min(values)
        pos = 0
    if kwargs.get("plot", True):
        plot_distribution(values, perc, pos, th, **kwargs)

    return th, perc, pos


def analyze_distribution(values, percentile=None, threshold=None, **kwargs):
    r"""
    Analyze the data to find what is the most suitable distribution type using
    Kolmogorov-Smirnov test.

    Arguments:
        values (np.array): List of values
        percentile (float): The percentile of cum sum down to which compute
            threshold. This argument is mutually exclusive with `threshold`.
        threshold (float): The value from which to select elements from the
            distribution. This argument is mutually exclusive with `percentile`.
        (Optional)
        plot (bool): Default is True
        verbose (bool): Default is False

    Return:
        Dictionary with keys: 'name' of the distribution, the
            'p_value' obtained in the test, the 'dist' itself as Callable, and
            the 'params' of the distribution. If parameter percentile is passed,
            the value from which the accumulated sum of values represent the
            percentage passed, under the key 'threshold'.
    """
    assert not (
        percentile is not None and threshold is not None
    ), "Both percentile and threshold cannot be specified at the same time."
    warnings.filterwarnings(action="ignore", category=RuntimeWarning)
    verbose = kwargs.get("verbose", False)
    d = dict()
    d["threshold"], d["percentile"], d["pos"] = get_boundaries(values, percentile, threshold, **kwargs)

    best_pvalue = 0.0
    for dist_name in [
        "norm",
        "exponweib",
        "weibull_max",
        "weibull_min",
        "pareto",
        "genextreme",
    ]:
        dist = getattr(stats, dist_name)
        param = dist.fit(values)
        # Applying the Kolmogorov-Smirnov test
        D, p = stats.kstest(values, dist_name, args=param)
        if p > best_pvalue:
            best_pvalue = p
            d["name"] = dist_name
            d["p_value"] = p
            d["dist"] = dist
            d["params"] = param
    if verbose:
        print(f"Best fitting distribution (p_val:{d['p_value']:.2f}): {d['name']}")
    return d


#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Reduce dataframe precision
"""
import numpy as np
import pandas as pd


def reduce_precision(df):
    """
    usage: give a dataframe, this fuction returns an optimized dataframe

    df = reduce_precision(df)

    reference: https://gist.github.com/enamoria/fa9baa906f23d1636c002e7186516a7b
    """
    cols_to_convert = []
    date_strings = ["_date", "date_", "date"]

    for col in df.columns:
        col_type = df[col].dtype
        if "string" not in col_type.name and col_type.name != "category" and "datetime" not in col_type.name:
            cols_to_convert.append(col)

    def _reduce_precision(x):
        col_type = x.dtype
        unique_data = list(x.unique())
        bools = [True, False, "true", "True", "False", "false"]
        n_unique = float(len(unique_data))
        n_records = float(len(x))
        cat_ratio = n_unique / n_records

        try:
            unique_data.remove(np.nan)
        except:
            pass

        if "int" in str(col_type):
            c_min = x.min()
            c_max = x.max()

            if c_min > np.iinfo(np.int8).min and c_max < np.iinfo(np.int8).max:
                x = x.astype(np.int8)
            elif c_min > np.iinfo(np.int16).min and c_max < np.iinfo(np.int16).max:
                x = x.astype(np.int16)
            elif c_min > np.iinfo(np.int32).min and c_max < np.iinfo(np.int32).max:
                x = x.astype(np.int32)
            elif c_min > np.iinfo(np.int64).min and c_max < np.iinfo(np.int64).max:
                x = x.astype(np.int64)

                # TODO: set precision to unsigned integers with nullable NA

        elif "float" in str(col_type):
            c_min = x.min()
            c_max = x.max()
            if c_min > np.finfo(np.float16).min and c_max < np.finfo(np.float16).max:
                x = x.astype(np.float16)
            elif c_min > np.finfo(np.float32).min and c_max < np.finfo(np.float32).max:
                x = x.astype(np.float32)
            else:
                x = x.astype(np.float64)
        elif "datetime" in col_type.name or any(i in str(x.name).lower() for i in date_strings):
            try:
                x = pd.to_datetime(x)
            except:
                pass
        elif any(i in bools for i in unique_data):
            x = x.astype("boolean")
            # TODO: set precision to bool if boolean not needed
        elif cat_ratio < 0.1 or n_unique < 20:
            x = x.astype("category")
        elif all(isinstance(i, str) for i in unique_data):
            x = x.astype("string")

        return x

    df[cols_to_convert] = df[cols_to_convert].apply(lambda x: _reduce_precision(x))

    return df
