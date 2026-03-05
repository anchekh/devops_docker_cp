require 'socket'

server = TCPServer.new(8080)
puts "Ruby server started on port 8080"
puts "Visit: http://localhost:8080"

loop do
    client = server.accept
    
    # Читаем запрос (нужно для корректной работы)
    request = client.gets
    
    # Отправляем ответ
    response = "HTTP/1.1 200 OK\r\n" +
               "Content-Type: text/html\r\n" +
               "Connection: close\r\n" +
               "\r\n" +
               "<h1>Hello, World!</h1>" +
               "<p>From Ruby Application</p>" +
               "<p>Time: #{Time.now}</p>"
    
    client.puts(response)
    client.close
end
