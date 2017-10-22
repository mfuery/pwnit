import {
    graphql,
} from 'react-relay';


const AllItemsQuery = graphql`
query AllItemsQuery {
    allItems {
        edges {
            node {
                id
                name
            }
        }
    }
  }
`;
