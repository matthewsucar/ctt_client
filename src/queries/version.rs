use serde::{Deserialize, Serialize};

pub struct GetVersion;
pub const OPERATION_NAME: &str = "GetVersion";
pub const QUERY : & str = "query GetVersion(){version}\n" ;
#[derive(Deserialize)]
pub struct ResponseData {
    pub version: Option<String>,
}

#[derive(Serialize,Deserialize,Debug, Default)]
pub struct Variables {}
impl graphql_client::GraphQLQuery for GetVersion {
    type Variables = Variables;
    type ResponseData = ResponseData;
    fn build_query(variables: Self::Variables) -> ::graphql_client::QueryBody<Self::Variables> {
        graphql_client::QueryBody {
            variables,
            query: QUERY,
            operation_name: OPERATION_NAME,
        }
    }
}
