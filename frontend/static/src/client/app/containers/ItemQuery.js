import {
    graphql,
} from 'react-relay';


const ItemQuery = graphql`
query ItemQuery($id: ID!) {
    item(id: $id) {
        id
        name
    }
  }
`;