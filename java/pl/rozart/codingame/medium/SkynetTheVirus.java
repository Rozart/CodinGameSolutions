import java.util.ArrayList;
import java.util.List;
import java.util.Optional;
import java.util.Scanner;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/
class SkynetTheVirus {

    private static List<Link> links = new ArrayList<>();
    private static List<Integer> gateways = new ArrayList<>();

    private static class Link{
        private int node1;
        private int node2;

        public Link(int node1, int node2){
            this.node1 = node1;
            this.node2 = node2;
        }

        public void cut(){
            System.out.println(this.node1 + " " + this.node2);
        }

        public boolean equals(Object object) {
            if (this == object) return true;
            if (object == null || getClass() != object.getClass()) return false;
            if (!super.equals(object)) return false;

            Link link = (Link) object;

            if (node1 != link.node1) return false;
            if (node2 != link.node2) return false;

            return true;
        }

        /**
         * Getter for property 'node1'.
         *
         * @return Value for property 'node1'.
         */
        public int getNode1() {
            return node1;
        }

        /**
         * Getter for property 'node2'.
         *
         * @return Value for property 'node2'.
         */
        public int getNode2() {
            return node2;
        }
    }

    public static Link getLinkConnectingAgentAndGateway(int agent){
        for(int currentGateway : gateways){
            Optional<Link> linkOptional = links.stream().filter(link -> (link.getNode1() == currentGateway && link.getNode2() == agent) || (link.getNode1() == agent && link.getNode2() == currentGateway)).findFirst();
            if(linkOptional.isPresent()){
                return linkOptional.get();
            }
        }
        return links.get(0);

    }

    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);

        int N = in.nextInt(); // the total number of nodes in the level, including the gateways
        int L = in.nextInt(); // the number of links
        int E = in.nextInt(); // the number of exit gateways
        for (int i = 0; i < L; i++) {
            int N1 = in.nextInt(); // N1 and N2 defines a link between these nodes
            int N2 = in.nextInt();
            links.add(new Link(N1, N2));
        }

        for (int i = 0; i < E; i++) {
            int EI = in.nextInt(); // the index of a gateway node
            gateways.add(EI);
        }

        // game loop
        while (true) {
            int SI = in.nextInt(); // The index of the node on which the Skynet agent is positioned this turn
            Link linkToCut = getLinkConnectingAgentAndGateway(SI);
            linkToCut.cut();
            links.remove(linkToCut);
        }
    }

}