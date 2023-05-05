export default class ChatApi {
    static async query_request(query) {
        const response = fetch("http://localhost:8000/query/"+query)
        return (await response).json()
    }
    static async direct_request(klass) {
        const response = fetch("http://localhost:8000/direct/"+klass)
        return (await response).json()
    }
}