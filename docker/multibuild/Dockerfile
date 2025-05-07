# 1 : Base Images
FROM golang:1.13 AS builder

# Step2 : Install dependencies
WORKDIR /go/src/github.com/asahiho/dockertext-greet

# Step3 : Build modules
COPY main.go .
RUN GOOS=linux go build -a -o greet .

## ----------------------------------
# 2 : Prooduction Image
FROM busybox
WORKDIR /opt/greet/bin

# Deploy modules
COPY --from=builder /go/src/github.com/asashiho/dockertext-greet .
ENTRYPOINT ["./greet"]
