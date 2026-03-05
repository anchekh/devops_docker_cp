FROM golang:1.16-alpine AS builder

WORKDIR /app
COPY main.go .
RUN go build -o hello-server main.go

FROM alpine:latest
WORKDIR /app
COPY --from=builder /app/hello-server .

EXPOSE 8080
CMD ["./hello-server"]
