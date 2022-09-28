import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.Set;

/**
 * Your implementation of various different graph algorithms.
 *
 * @author SAHEJ PANAG
 * @version 1.0
 * @userid spanag3
 * @GTID 903604843
 *
 * Collaborators: NONE
 *
 * Resources: Canvas
 */
public class GraphAlgorithms {

    /**
     * Performs a breadth first search (bfs) on the input graph, starting at
     * the parameterized starting vertex.
     *
     * When exploring a vertex, explore in the order of neighbors returned by
     * the adjacency list. Failure to do so may cause you to lose points.
     *
     * You may import/use java.util.Set, java.util.List, java.util.Queue, and
     * any classes that implement the aforementioned interfaces, as long as they
     * are efficient.
     *
     * The only instance of java.util.Map that you may use is the
     * adjacency list from graph. DO NOT create new instances of Map
     * for BFS (storing the adjacency list in a variable is fine).
     *
     * DO NOT modify the structure of the graph. The graph should be unmodified
     * after this method terminates.
     *
     * @param <T>   the generic typing of the data
     * @param start the vertex to begin the bfs on
     * @param graph the graph to search through
     * @return list of vertices in visited order
     * @throws IllegalArgumentException if any input is null, or if start
     *                                  doesn't exist in the graph
     */
    public static <T> List<Vertex<T>> bfs(Vertex<T> start, Graph<T> graph) {
        if (start == null || graph == null) {
            throw new IllegalArgumentException("One of the inputs is null");
        }
        Map<Vertex<T>, List<VertexDistance<T>>> adjList = graph.getAdjList();
        if (!adjList.containsKey(start)) {
            throw new IllegalArgumentException("start key is not in graph");
        }
        Queue<Vertex<T>> q = new LinkedList<>();
        List<Vertex<T>> visitedList = new LinkedList<>();
        Set<Vertex<T>> visitedSet = new HashSet<>();
        q.add(start);
        while (!q.isEmpty() && visitedList.size() != adjList.size()) {
            Vertex<T> v = q.remove();
            if (!(visitedSet.contains(v))) {
                visitedList.add(v);
                visitedSet.add(v);
                for (VertexDistance<T> adj : adjList.get(v)) {
                    Vertex<T> w = adj.getVertex();
                    if (!visitedSet.contains(w)) {
                        q.add(w);
                    }
                }
            }
        }
        return visitedList;
    }

    /**
     * Performs a depth first search (dfs) on the input graph, starting at
     * the parameterized starting vertex.
     *
     * When exploring a vertex, explore in the order of neighbors returned by
     * the adjacency list. Failure to do so may cause you to lose points.
     *
     * *NOTE* You MUST implement this method recursively, or else you will lose
     * all points for this method.
     *
     * You may import/use java.util.Set, java.util.List, and
     * any classes that implement the aforementioned interfaces, as long as they
     * are efficient.
     *
     * The only instance of java.util.Map that you may use is the
     * adjacency list from graph. DO NOT create new instances of Map
     * for DFS (storing the adjacency list in a variable is fine).
     *
     * DO NOT modify the structure of the graph. The graph should be unmodified
     * after this method terminates.
     *
     * @param <T>   the generic typing of the data
     * @param start the vertex to begin the dfs on
     * @param graph the graph to search through
     * @return list of vertices in visited order
     * @throws IllegalArgumentException if any input is null, or if start
     *                                  doesn't exist in the graph
     */
    public static <T> List<Vertex<T>> dfs(Vertex<T> start, Graph<T> graph) {
        if (start == null || graph == null) {
            throw new IllegalArgumentException("one or both inputs are equals to null");
        }
        Map<Vertex<T>, List<VertexDistance<T>>> adjList = graph.getAdjList();
        if (!adjList.containsKey(start)) {
            throw new IllegalArgumentException("start key is not in graph");
        }
        Set<Vertex<T>> vS = new HashSet<>();
        List<Vertex<T>> toReturn = new LinkedList<>();
        realDfs(start, adjList, toReturn, vS);

        return toReturn;
    }

    /**
     * Recursive helper method for dfs.
     *
     * @param start the vertex to begin dfs on
     * @param adjList the adjacent list
     * @param toReturn the visited list to return
     * @param vS the visited set
     * @param <T> generic type
     */
    private static <T> void realDfs(Vertex<T> start, Map<Vertex<T>, List<VertexDistance<T>>> adjList,
                                    List<Vertex<T>> toReturn, Set<Vertex<T>> vS) {
        vS.add(start);
        toReturn.add(start);
        for (VertexDistance<T> adj : adjList.get(start)) {
            Vertex<T> w = adj.getVertex();
            if (!(vS.contains(w))) {
                realDfs(w, adjList, toReturn, vS);
            }
        }
    }

    /**
     * Finds the single-source shortest distance between the start vertex and
     * all vertices given a weighted graph (you may assume non-negative edge
     * weights).
     *
     * Return a map of the shortest distances such that the key of each entry
     * is a node in the graph and the value for the key is the shortest distance
     * to that node from start, or Integer.MAX_VALUE (representing
     * infinity) if no path exists.
     *
     * You may import/use java.util.PriorityQueue,
     * java.util.Map, and java.util.Set and any class that
     * implements the aforementioned interfaces, as long as your use of it
     * is efficient as possible.
     *
     * You should implement the version of Dijkstra's where you use two
     * termination conditions in conjunction.
     *
     * 1) Check if all of the vertices have been visited.
     * 2) Check if the PQ is empty yet.
     *
     * DO NOT modify the structure of the graph. The graph should be unmodified
     * after this method terminates.
     *
     * @param <T>   the generic typing of the data
     * @param start the vertex to begin the Dijkstra's on (source)
     * @param graph the graph we are applying Dijkstra's to
     * @return a map of the shortest distances from start to every
     * other node in the graph
     * @throws IllegalArgumentException if any input is null, or if start
     *                                  doesn't exist in the graph.
     */
    public static <T> Map<Vertex<T>, Integer> dijkstras(Vertex<T> start,
                                                        Graph<T> graph) {
        if (start == null || graph == null) {
            throw new IllegalArgumentException("one or both inputs are invalid");
        }
        Map<Vertex<T>, List<VertexDistance<T>>> adjList = graph.getAdjList();
        if (!adjList.containsKey(start)) {
            throw new IllegalArgumentException("start key is not in the graph");
        }
        Queue<VertexDistance<T>> pQ = new PriorityQueue<>();
        Map<Vertex<T>, Integer> map = new HashMap<>();
        Set<Vertex<T>> vS = new HashSet<>();
        for (Vertex<T> v: graph.getVertices()) {
            map.put(v, Integer.MAX_VALUE);
        }
        pQ.add(new VertexDistance<T>(start, 0));
        while (!pQ.isEmpty() && vS.size() != graph.getVertices().size()) {
            VertexDistance<T> curr = pQ.remove();
            if (!vS.contains(curr.getVertex())) {
                vS.add(curr.getVertex());
                map.put(curr.getVertex(), curr.getDistance());
                for (VertexDistance<T> w : adjList.get(curr.getVertex())) {
                    if (!vS.contains(w.getVertex())) {
                        pQ.add(new VertexDistance<T>(w.getVertex(), curr.getDistance() + w.getDistance()));
                    }
                }
            }
        }
        return map;
    }

    /**
     * Runs Kruskal's algorithm on the given graph and returns the Minimal
     * Spanning Tree (MST) in the form of a set of Edges. If the graph is
     * disconnected and therefore no valid MST exists, return null.
     *
     * You may assume that the passed in graph is undirected. In this framework,
     * this means that if (u, v, 3) is in the graph, then the opposite edge
     * (v, u, 3) will also be in the graph, though as a separate Edge object.
     *
     * The returned set of edges should form an undirected graph. This means
     * that every time you add an edge to your return set, you should add the
     * reverse edge to the set as well. This is for testing purposes. This
     * reverse edge does not need to be the one from the graph itself; you can
     * just make a new edge object representing the reverse edge.
     *
     * You may assume that there will only be one valid MST that can be formed.
     *
     * Kruskal's will also require you to use a Disjoint Set which has been
     * provided for you. A Disjoint Set will keep track of which vertices are
     * connected given the edges in your current MST, allowing you to easily
     * figure out whether adding an edge will create a cycle. Refer
     * to the DisjointSet and DisjointSetNode classes that
     * have been provided to you for more information.
     *
     * You should NOT allow self-loops or parallel edges into the MST.
     *
     * By using the Disjoint Set provided, you can avoid adding self-loops and
     * parallel edges into the MST.
     *
     * You may import/use java.util.PriorityQueue,
     * java.util.Set, and any class that implements the aforementioned
     * interfaces.
     *
     * DO NOT modify the structure of the graph. The graph should be unmodified
     * after this method terminates.
     *
     * @param <T>   the generic typing of the data
     * @param graph the graph we are applying Kruskals to
     * @return the MST of the graph or null if there is no valid MST
     * @throws IllegalArgumentException if any input is null
     */
    public static <T> Set<Edge<T>> kruskals(Graph<T> graph) {
        if (graph == null) {
            throw new IllegalArgumentException("graph is equal to null change input");
        }
        DisjointSet<Vertex<T>> dS = new DisjointSet<>();
        Queue<Edge<T>> pQ = new PriorityQueue<>();
        Set<Edge<T>> mst = new HashSet<>();
        int n = graph.getVertices().size();
        for (Edge<T> edge : graph.getEdges()) {
            pQ.add(edge);
        }
        while (!(pQ.isEmpty()) && mst.size() < 2 * (n - 1)) {
            Edge<T> edge = pQ.remove();
            if (!(dS.find(edge.getU()).equals(dS.find(edge.getV())))) {
                mst.add(edge);
                mst.add(new Edge<T>(edge.getV(), edge.getU(), edge.getWeight()));
                dS.union(edge.getU(), edge.getV());
            }
        }
        if (mst.size() != 2 * (n - 1)) {
            return null;
        }
        return mst;
    }
}
