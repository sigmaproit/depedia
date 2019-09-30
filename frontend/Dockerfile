FROM nginx:stable-alpine

COPY nginx.conf /etc/nginx/conf.d/default.conf

RUN apk add --update npm
WORKDIR /dm-app
COPY package.json /dm-app/package.json
RUN npm install
RUN npm install -g @angular/cli@8.1.1

COPY . /dm-app

RUN npm run build -- --project=dm-app --prod
RUN cp -R dist/dm-app/* /usr/share/nginx/html/
