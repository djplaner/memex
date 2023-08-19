# local-canvas-dev

See also: [[canvas-development]]

## docker - mac 

 Running Canvas:

    docker-compose up -d
    open http://canvas.docker

  Running the tests:

    docker-compose run --rm web bundle exec rspec

   Running Selenium tests:

    add docker-compose/selenium.override.yml in the .env file
      echo ':docker-compose/selenium.override.yml' >> .env

    build the selenium container
      docker-compose up -d selenium-hub

    run selenium
      docker-compose run --rm web bundle exec rspec spec/selenium

    Virtual network remote desktop sharing to selenium container
      for Firefox:
        $ open vnc://secret:secret@seleniumff.docker
      for chrome:
        $ open vnc://secret:secret@seleniumch.docker:5901

  I'm stuck. Where can I go for help?

    FAQ:           https://github.com/instructure/canvas-lms/wiki/FAQ
    Dev & Friends: http://instructure.github.io/
    Canvas Guides: https://guides.instructure.com/
    Vimeo channel: https://vimeo.com/canvaslms
    API docs:      https://canvas.instructure.com/doc/api/index.html
    Mailing list:  http://groups.google.com/group/canvas-lms-users
    IRC:           https://web.libera.chat/#canvas-lms

    Please do not open a GitHub issue until you have tried asking for help on
    the mailing list or IRC - GitHub issues are for verified bugs only.
    Thanks and good luck!
  
## Local dev 

Token - mpH4O1mxzC0mwnp071wOLWsMREpi2SSTwhSK61yGC9IqiUOnRW96Io0bro0SZk4H

To test that it's all working 
curl http://canvas.docker/api/v1/users/self -H "Authorization: Bearer mpH4O1mxzC0mwnp071wOLWsMREpi2SSTwhSK61yGC9IqiUOnRW96Io0bro0SZk4H"