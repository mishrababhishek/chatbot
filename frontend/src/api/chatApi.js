export default class ChatApi {
    static async query_request(query) {
        try {
            const response = fetch("http://localhost:8000/query/"+query)
            return (await response).json()    
        } catch (error) {
            return "Sorry!, Something not feels Right. Please Try After Sometime"
        }
        
    }
    static async direct_request(klass) {
        try {
            const response = fetch("http://localhost:8000/direct/"+klass)
            return (await response).json()    
        } catch (error) {
            return "Sorry!, Something not feels Right. Please Try After Sometime"
        }
    }
}